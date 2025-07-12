<!-- all html docs must start with <!DOCTYPE html> -->
<!DOCTYPE html> 

<!-- the html tag defines the whole of an html doc, everything must be nested within it -->
<html>
    <!-- the head tag is a container for metadata -->
    <head>
        <title>This tag adds a title to a page</title>
    </head>
<!-- the body tag defines the visible part of an html doc,
  basically if something is nested within the body it will appear to the user -->
<body>
    
<!-- elements define things in html, most start & end with a tag -->

<p> <!-- this tag is the start of an element that defines a paragraph -->
<!-- everything within the start & end tags is called that element's content -->
I am the content of this paragraph element.
</p> <!-- this is the end of the paragraph element  -->

<!-- elements can have attributes, which are specified within the start tag of an element -->

<!-- this 'a' tag it defines a hyperlink, & has an attribute, href, which specifies the URL of the hyperlink  -->
<a href="/">click to go nowhere</a>

<!-- Notable attributes

    title="The value of this attribute is displayed as tooltip when moused over"

    src="This attribute specifies the path to a 'source' file, it can be used with absolute urls, or relative urls"
    note on relative urls, if they start with a slash the url will be relative to the domain, 
    without a slash it will be relative to the current page.

    lang="This attribute defines the language of a html doc, it is use in the html tag"

    target=""
    The target attribute specifies where to open a linked document, the default is _self, which opens the linked doc in the same tab
    _blank opens the doc in a new tab

    _parent opens in the parent frame

    _top opens in the full body of the window

    href can be used to make page bookmarks.
    <h2 id="C4">Chapter 4</h2>
    <a href="#C4">Jump to Chapter 4</a>
    
-->

<!-- Using headers is important for search engines, look more into this. -->

<h1>This is the biggest, therefore most important heading</h1>
<h6>This is the smallest, therefore the least important heading</h6>
<hr>
<br>
<p>p tags always start on a new line</p>
<hr>

<!-- use the pre tag for defining preformatted text -->
<pre>

    This text

    will
                look
        like
    This        on the          page

</pre>

<!-- different formatting tags -->
<b> Bold text</b>
<br>
<strong>Important text</strong>
<br>
<i>Italic text </i>
<br>
<em>Emphasized text </em>
<br>
<mark>Marked text </mark>
<br>
<small>Smaller text </small>
<br>
<del>Deleted text </del>
<br>
<ins>Inserted text </ins>
<br>
<sub>Subscript text </sub>
<br>
<sup>Superscript text </sup>
<br>

<p>Image maps are used to create clickable areas within an image</p>
        <!-- 

        <img src="workplace.jpg" alt="Workplace" usemap="#workmap">

        <map name="workmap">
            <area shape="circle" coords="337,300,44" href="coffee.htm" onclick="myFunction()">
        </map>

        --> 
        
        <p>A picture element contains one or more source elements, the picture element is used to display different images for different devices or screen sizes.</p>

        <!--
        
            this picture element offers different formats for the browser 
            <picture>
                <source srcset="img_avatar.png">
                <source srcset="img_girl.jpg">
                <img src="img_beatles.gif" alt="Beatles" style="width:auto;">
            </picture>

            this element offers different images depeneding on size
            
            <picture>
                <source media="(min-width: 650px)" srcset="img_food.jpg">
                <source media="(min-width: 465px)" srcset="img_car.jpg">
                <img src="img_girl.jpg">
            </picture>

        -->

</body>

</html>