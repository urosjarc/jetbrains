#PRO.Intellij
Settings for all Intellij IDE-s

##System settings
 - https://confluence.jetbrains.com/display/IDEADEV/Inotify+Watches+Limit

##Plugins
 - ideavim
 - .ignore
 - Key promoter
 - CodeGlance
 - Markdown
 - https://github.com/jkaving/intellij-colors-solarized

##Modified settings

    Appearance & Begavior > Appearance > Override default fonts by >
                                                                   > Name(Dialog)
                                                                   > Size(10)
                                                                   > Theme(Darcula)
                                       > Animate window(FALSE)
                               
    Editor > Colors & Fonts > Font > 
                                   > Size(11)
                                   > Line spacing(1)
                                   > Scheme(Solarized Light)
           > Code Style > 
                        > Use tab character(TRUE)
                        > Smart tabs(TRUE)
           > General > Code Completion >
                                       > Autopopup in (ms):(TRUE,0)
           	     > Code Folding >
                                    > Documentation comments(TRUE)
                          	    > Method bodies(TRUE)
                                    > Custom folding regions(TRUE)

    Version Control > GitHub > 
                             > Login(*)
                             > Password(*)

    Other settings > Vim Emulation >
				   > *(IDE)
				   > Replace...(VIM)

    Keymaps >
            > Clone caret up      <ALT>Num-
            > Clone caret dow.    <ALT>Num+
            > Search everywhere   <ALT>s
            > Find action         <ALT>a
            > Find in project     <ALT>p
            > Switcher            <ALT><TAB>
            > Comment line        <ALT>/
            > Comment block       <ALT><S>/

    >>> JavaScript

    Languages & Frameworks > Node.js and NPM >
                                             > Sources of Node.js Core Modules(SET)
                                             
    
##Modified configuration
    View > Navigation bar(FALSE)
         > Status bar(FALSE)
         > Active editor > Show line numbers(TRUE)
    Window > Editor Tabs > Tabs Placement > Show tabs in single row(FALSE)
    <project gear> > 
                   > Sort by type(TRUE)
                   
    ---> Set every (View > Tool Window > * ) to show
    ---> Set every (-//- > Tool Window > *, not Structure) to Docked mode(FALSE)
    

##Snipets
    Settings > Editor > Live Templates

##Shortcuts

####Hellper
    Intention act.  <ALT><ENTER>

####Multiple cursors
    Mouse select    <ALT><MR>
    Find under cur. <ALT>j
    Unsel. chosen.  <ALT><S>j
    Up              <ALT>Num-
    Down            <ALT>Num+

####Find

    Search      <ALT>s
    Action		<ALT>a	
    In project  <ALT>p

####Navigate
    Switcher    <ALT><TAB>
    Project     <ALT>1

####Code jumps
    To defini.  <C>b

####Editing
    Commenting  <ALT>/
    Block comm. <ALT><S>/
