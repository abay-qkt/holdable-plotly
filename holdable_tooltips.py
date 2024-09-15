from pathlib import Path
from IPython.display import display
from IPython.display import IFrame,HTML

def export_html(fig, 
                filename="", 
                show_custom=True,
                show_hovercustom=False,
                include_plotlyjs='cdn',
                include_mathjax =False,
                display_height=None, 
                div_id=None):

    js_str = """
    var myPlot = document.getElementById("{plot_id}")
    //CUSTOM var myData = document.getElementById("custom_{plot_id}")
    var is_selected = false;
    myPlot.on('plotly_click', function(data){
    is_selected = !is_selected;
    if(is_selected){
        myPlot.on('plotly_beforehover',function(){return false;});
        console.log(data.points[data.points.length-1].customdata)
        //CUSTOM myData.innerHTML = data.points[data.points.length-1].customdata;
    }else{
        myPlot.on('plotly_beforehover',function(){return true;});
        //CUSTOM myData.innerHTML = "";
    }
    });
    myPlot.on('plotly_hover', function(data){
        //CUSTOM //HOVER myData.innerHTML = data.points[data.points.length-1].customdata;
    });
    """
     
    if(filename==""):
        filename = "temporary_plotly_file.html"        
    if(show_custom):
        js_str = js_str.replace("//CUSTOM ","")
    if(show_hovercustom):
        js_str = js_str.replace("//HOVER ","")
        
    if(div_id):
        plotly_div = fig.to_html(full_html=False,
                                 post_script=js_str,
                                 include_plotlyjs=False,
                                 include_mathjax=False)
    else:
        plotly_div = fig.to_html(full_html=False,
                                 post_script=js_str,
                                 include_plotlyjs=include_plotlyjs,
                                 include_mathjax=include_mathjax)
    
    plotly_div_id = plotly_div.split('div id="')[1].split('"')[0]
    elements = plotly_div
    if(show_custom):
        elements = elements.replace("<div>",'<div id="main_{}" align="center">'.format(plotly_div_id))
        ele = '</div>\n<div id="custom_{}"></div>'.format(plotly_div_id)
        elements = elements.replace("</div>",ele,1)
        
    if(div_id):
        return elements
    else:
        with open(filename,"w") as f:
            f.write(elements)
    
    if(display_height is not None):
        if(display_height==True):
            display_height = fig.layout.height+20
        with open(filename) as f:
            html = f.read()
        display(HTML(html))
        return filename 
        