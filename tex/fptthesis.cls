%% fptthesis.cls -- FPT University capstone thesis class (AIP491).
%% Structure: Template_AIP491_CP_StudentsGuide (school).
%% Typography: CS-Thesis_Template "Style Guidelines" (supervisor's template).
%% Every length below is measured from those two files; see rules/01-format.md.
%% All lengths use bp (1/72 in), the unit Word calls "pt".
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{fptthesis}[2026/11/25 v1.0 FPT University capstone thesis]

%% ---- Options -------------------------------------------------------------
\newif\iffpt@letter \fpt@letterfalse
\newif\iffpt@arabic \fpt@arabicfalse
\newif\iffpt@nobreak \fpt@nobreakfalse
\DeclareOption{a4paper}{\fpt@letterfalse}
\DeclareOption{letterpaper}{\fpt@lettertrue}
% Roman = school numbering (I. / 1. / 1.1); arabic = supervisor's (1 / 1.1 / 1.1.1)
\DeclareOption{romanchapters}{\fpt@arabicfalse}
\DeclareOption{arabicchapters}{\fpt@arabictrue}
% The school starts each part on a new page; the supervisor's sample does not.
\DeclareOption{chapterbreak}{\fpt@nobreakfalse}
\DeclareOption{nochapterbreak}{\fpt@nobreaktrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax
\LoadClass[11pt,oneside]{report}

\RequirePackage{iftex}
\ifXeTeX\else\ifLuaTeX\else
  \ClassError{fptthesis}{XeLaTeX is required}{Build with latexmk (see README.md).}%
\fi\fi
\RequirePackage{etoolbox}
\RequirePackage{calc}

%% ---- Version and mode (written by latexmkrc) -----------------------------
\providecommand\ThesisVersion{unversioned}
\providecommand\ThesisCommit{unknown}
\providecommand\ThesisMode{draft}
\InputIfFileExists{version.tex}{}{}
\newif\ifthesisfinal \thesisfinalfalse
\ifdefstring{\ThesisMode}{final}{\thesisfinaltrue}{}

%% ---- Page ----------------------------------------------------------------
\iffpt@letter
  \RequirePackage[letterpaper]{geometry}
\else
  \RequirePackage[a4paper]{geometry}
\fi
\geometry{left=90bp,right=90bp,top=72bp,bottom=72bp,
  headheight=12bp,headsep=24.95bp,footskip=34.2bp}

%% ---- Fonts ---------------------------------------------------------------
\RequirePackage{amsmath}
\RequirePackage{fontspec}
\RequirePackage{unicode-math}
\defaultfontfeatures{Ligatures={TeX,NoCommon}}
% \fpt@font{setter}{name in Word}{fallback shipped with TeX Live}{fallback extension pattern}
\newcommand\fpt@fontset{MS}
\IfFontExistsTF{Times New Roman}{\setmainfont{Times New Roman}}{%
  \gdef\fpt@fontset{fallback}%
  \setmainfont{texgyretermes}[Extension=.otf,UprightFont=*-regular,BoldFont=*-bold,
    ItalicFont=*-italic,BoldItalicFont=*-bolditalic]}
\IfFontExistsTF{Arial}{\setsansfont{Arial}}{%
  \gdef\fpt@fontset{fallback}%
  \setsansfont{texgyreheros}[Extension=.otf,UprightFont=*-regular,BoldFont=*-bold,
    ItalicFont=*-italic,BoldItalicFont=*-bolditalic]}
\IfFontExistsTF{Courier New}{\setmonofont{Courier New}[Ligatures=NoCommon]}{%
  \gdef\fpt@fontset{fallback}%
  \setmonofont{texgyrecursor}[Extension=.otf,UprightFont=*-regular,BoldFont=*-bold,
    ItalicFont=*-italic,BoldItalicFont=*-bolditalic]}
% The school cover keeps its own two faces.
\IfFontExistsTF{Calibri}{\newfontfamily\fpt@calibri{Calibri}}{%
  \newfontfamily\fpt@calibri{Carlito}[Extension=.ttf,UprightFont=*-Regular,BoldFont=*-Bold,
    ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]}
\IfFontExistsTF{Cambria}{\newfontfamily\fpt@cambria{Cambria}}{%
  \newfontfamily\fpt@cambria{Caladea}[Extension=.ttf,UprightFont=*-Regular,BoldFont=*-Bold,
    ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]}
\setmathfont{texgyretermes-math.otf}
\AtBeginDocument{\typeout{FPTTHESIS fontset=\fpt@fontset\space mode=\ThesisMode\space version=\ThesisVersion}}

\newcommand\fpt@size[2]{\fontsize{#1bp}{#2bp}\selectfont}
\renewcommand\normalsize{\fpt@size{11}{12.65}%
  \abovedisplayskip 8bp plus 2bp minus 2bp \belowdisplayskip\abovedisplayskip
  \abovedisplayshortskip 4bp plus 2bp \belowdisplayshortskip 6bp plus 2bp minus 2bp}
\renewcommand\small{\fpt@size{10}{11.5}}
\renewcommand\footnotesize{\fpt@size{9}{10.35}}
\renewcommand\scriptsize{\fpt@size{8}{9.2}}
\normalsize

%% ---- Paragraphs (style "Normal": justified, single, 12 pt apart) ---------
\setlength\parindent{0pt}
\setlength\parskip{12.05bp}
\setlength\topskip{10.1bp}
\raggedbottom
\clubpenalty=10000 \widowpenalty=10000 \displaywidowpenalty=10000
% Word does not hyphenate; neither do the two templates.
\frenchspacing
\hyphenpenalty=10000 \exhyphenpenalty=500 \tolerance=2000 \emergencystretch=3em
\RequirePackage[british]{babel}
\RequirePackage[autostyle=true,english=british]{csquotes}

%% ---- Headings (H1 Arial bold 16, H2 13, H3 11) ----------------------------
\RequirePackage{titlesec}
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{1}
\iffpt@arabic
  \renewcommand\thechapter{\arabic{chapter}}
  \renewcommand\thesection{\thechapter.\arabic{section}}
  \renewcommand\thesubsection{\thesection.\arabic{subsection}}
  \newcommand\fpt@chaplabel{\thechapter}
  \newcommand\fpt@seclabel{\thesection}
\else
  \renewcommand\thechapter{\Roman{chapter}}
  \renewcommand\thesection{\arabic{section}}
  \renewcommand\thesubsection{\thesection.\arabic{subsection}}
  \renewcommand\p@section{\thechapter.}
  \renewcommand\p@subsection{\thechapter.}
  \newcommand\fpt@chaplabel{\thechapter.}
  \newcommand\fpt@seclabel{\thesection.}
\fi
\newlength\fpt@labelwd
% number in a hanging box: at least #1 wide (Word's hanging indent), wider if needed
\newcommand\fpt@numbox[2]{%
  \settowidth\fpt@labelwd{#2\hspace{0.35em}}%
  \ifdim\fpt@labelwd<#1\relax\setlength\fpt@labelwd{#1}\fi
  \makebox[\fpt@labelwd][l]{#2}}
\newcommand\fpt@hone{\sffamily\bfseries\fpt@size{16}{18.4}\raggedright}
\newcommand\fpt@htwo{\sffamily\bfseries\fpt@size{13}{14.95}\raggedright}
\newcommand\fpt@hthree{\sffamily\bfseries\fpt@size{11}{12.65}\raggedright}
\titleformat{\chapter}[hang]{\fpt@hone}{\fpt@numbox{21.55bp}{\fpt@chaplabel}}{0pt}{}
\titleformat{name=\chapter,numberless}[hang]{\fpt@hone}{}{0pt}{}
\titleformat{\section}[hang]{\fpt@htwo}{\rule{0pt}{12.26bp}\fpt@numbox{28.9bp}{\fpt@seclabel}}{0pt}{}
\titleformat{\subsection}[hang]{\fpt@hthree}{\fpt@numbox{36bp}{\thesubsection}}{0pt}{}
\iffpt@nobreak
  \titleclass{\chapter}{straight}
  \titlespacing*{\chapter}{0pt}{16.85bp}{-0.35bp}
\else
  \titlespacing*{\chapter}{0pt}{-7.5bp}{-0.35bp}
\fi
\titlespacing*{\section}{0pt}{5.5bp}{-5.65bp}
\titlespacing*{\subsection}{0pt}{0bp}{-5.65bp}
% Only three heading levels exist; deeper ones are a layout error.
\renewcommand\subsubsection{\ClassError{fptthesis}{Only three heading levels are allowed}{See rules/01-format.md.}}
\renewcommand\paragraph{\ClassError{fptthesis}{Only three heading levels are allowed}{See rules/01-format.md.}}

%% ---- Header / footer (Times New Roman 9) ----------------------------------
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{xcolor}
\definecolor{fptguide}{HTML}{0000FF}
\definecolor{fpttodo}{HTML}{C00000}
\definecolor{fptstamp}{HTML}{808080}
\definecolor{fpthead}{HTML}{FFE8E1}
\definecolor{fptrule}{HTML}{4F81BD}
\newcommand\fpt@hf{\normalfont\fpt@size{9}{10.35}}
\newcommand\fpt@stamp{\ifthesisfinal\else
  \fpt@hf\color{fptstamp}\fpt@size{7}{8}DRAFT \ThesisVersion\fi}
\renewcommand\headrulewidth{0pt}
\renewcommand\footrulewidth{0pt}
\fancypagestyle{fptfront}{\fancyhf{}%
  \fancyhead[L]{\fpt@hf\fpt@get{title}}\fancyhead[R]{\fpt@hf\fpt@get{headerauthor}}%
  \fancyfoot[C]{\fpt@stamp}}
\fancypagestyle{fptmain}{\fancyhf{}%
  \fancyhead[L]{\fpt@hf\fpt@get{title}}\fancyhead[R]{\fpt@hf\fpt@get{headerauthor}}%
  \fancyfoot[L]{\fpt@hf\thepage\ of \pageref*{LastPage}}%
  \fancyfoot[C]{\fpt@stamp}%
  \fancyfoot[R]{\fpt@hf\fpt@get{date}}}
\fancypagestyle{plain}[fptmain]{}
\newcommand\frontmatter{\cleardoublepage\pagestyle{fptfront}\fancypagestyle{plain}[fptfront]{}}
\newcommand\mainmatter{\clearpage\pagestyle{fptmain}\fancypagestyle{plain}[fptmain]{}%
  \iffpt@nobreak\vspace*{-24.5bp}\fi}

%% ---- Lists (bullet at 18 pt, text at 36 pt) -------------------------------
\RequirePackage{enumitem}
\setlist{parsep=0pt,topsep=0.6bp,partopsep=0pt,itemsep=12.8bp,leftmargin=36bp,labelwidth=18bp,labelsep=0pt,align=left,
  before=\setlength\parskip{12.05bp},listparindent=0pt}
\setlist[itemize,1]{label={\fpt@size{13.5}{12.65}\textbullet}}
\setlist[itemize,2]{label=\textopenbullet}
\setlist[enumerate,1]{label=\arabic*.}
\setlist[enumerate,2]{label=(\alph*)}

%% ---- Floats and captions (style "figure": centred italic, "Figure 1.") ----
\RequirePackage{graphicx}
\graphicspath{{figures/}}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{float}
\captionsetup{font={it},labelfont={it},labelsep=period,justification=centering,singlelinecheck=off,
  figureposition=below,tableposition=above,skip=6bp}
\captionsetup[subfigure]{font={it,small},labelfont={it,small},labelformat=simple,labelsep=space}
\renewcommand\thesubfigure{(\alph{subfigure})}
\counterwithout{figure}{chapter}
\counterwithout{table}{chapter}
\counterwithout{equation}{chapter}
\setlength\textfloatsep{18bp plus 2bp minus 2bp}
\setlength\floatsep{18bp plus 2bp minus 2bp}
\setlength\intextsep{18bp plus 2bp minus 2bp}
% [H]: same gap above and below; the paragraph after the float adds \parskip itself
\renewcommand\float@endH{\@endfloatbox\vskip\intextsep
  \if@flstyle\setbox\@currbox\float@makebox\columnwidth\fi
  \box\@currbox\vskip\glueexpr\intextsep-\parskip\relax}
\renewcommand\topfraction{.85}\renewcommand\bottomfraction{.7}
\renewcommand\textfraction{.1}\renewcommand\floatpagefraction{.75}

%% ---- Tables ---------------------------------------------------------------
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{multirow}
\RequirePackage{colortbl}
\RequirePackage{siunitx}
\sisetup{group-separator={,},group-minimum-digits=4,detect-all}
\AtBeginEnvironment{tabular}{\small}
\AtBeginEnvironment{tabularx}{\small}
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcolumntype{C}{>{\centering\arraybackslash}X}
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}
% numbers explained below a table or figure
\newcommand\fignote[1]{\par\vspace{4bp}{\footnotesize\normalfont\raggedright #1\par}}

%% ---- Code (style "Code": Courier New 9, single, 0.25 in indents) ----------
\RequirePackage{listings}
\lstdefinestyle{fpt}{basicstyle=\ttfamily\fpt@size{9}{10.2},columns=fullflexible,keepspaces=true,
  breaklines=true,breakatwhitespace=false,showstringspaces=false,tabsize=2,
  xleftmargin=17.85bp,xrightmargin=17.85bp,aboveskip=12bp,belowskip=0bp,
  frame=none,numbers=none,extendedchars=true,upquote=true,captionpos=b}
\lstset{style=fpt}
\lstdefinelanguage{TypeScript}{morekeywords={},sensitive=true}
\lstset{numberbychapter=false}

%% ---- Algorithms -----------------------------------------------------------
\RequirePackage{algorithm}
\RequirePackage{algpseudocode}
\AtBeginEnvironment{algorithmic}{\small}
\floatstyle{plaintop}\restylefloat{algorithm}

%% ---- Table of contents (Arial 11 / 10) ------------------------------------
\RequirePackage{titletoc}
\contentsmargin{0pt}
\newif\iffpt@afterchap
\newcommand\fpt@tocdots{\titlerule*[2.78bp]{.}\thecontentspage\@gobble}
\iffpt@arabic\newcommand\fpt@dot{}\else\newcommand\fpt@dot{.}\fi
\titlecontents{chapter}[22.1bp]{\sffamily\fpt@size{11}{12.65}\addvspace{12.05bp}\global\fpt@afterchaptrue}
  {\hspace*{-22.1bp}\fpt@numbox{22.1bp}{\thecontentslabel\fpt@dot}}{\hspace*{-22.1bp}}{\fpt@tocdots\contentspage}
\titlecontents{section}[54.1bp]{\sffamily\fpt@size{10}{11.5}%
  \iffpt@afterchap\addvspace{10.8bp}\global\fpt@afterchapfalse\else\addvspace{12.05bp}\fi}
  {\hspace*{-32bp}\fpt@numbox{32bp}{\thecontentslabel\fpt@dot}}{\hspace*{-32bp}}{\fpt@tocdots\contentspage}
\titlecontents{subsection}[86bp]{\sffamily\fpt@size{10}{11.5}\addvspace{12.05bp}}
  {\hspace*{-32bp}\fpt@numbox{32bp}{\thecontentslabel}}{\hspace*{-32bp}}{\fpt@tocdots\contentspage}
\titlecontents{figure}[54bp]{\sffamily\fpt@size{10}{11.5}\addvspace{6bp}}
  {\hspace*{-54bp}\fpt@numbox{54bp}{Figure \thecontentslabel.}}{}{\fpt@tocdots\contentspage}
\titlecontents{table}[54bp]{\sffamily\fpt@size{10}{11.5}\addvspace{6bp}}
  {\hspace*{-54bp}\fpt@numbox{54bp}{Table \thecontentslabel.}}{}{\fpt@tocdots\contentspage}

%% ---- References (Harvard, Curtin guide supplied by the supervisor) --------
\RequirePackage[backend=biber,style=fptharvard]{biblatex}
\setlength\bibhang{22bp}
\setlength\bibitemsep{0pt}
\setcounter{biburlnumpenalty}{9000}
\setcounter{biburlucpenalty}{9000}
\setcounter{biburllcpenalty}{9000}

%% ---- Links and cross-references -------------------------------------------
\RequirePackage[hidelinks,unicode,bookmarksnumbered,pdfusetitle=false]{hyperref}
\RequirePackage{bookmark}
\RequirePackage[nameinlink]{cleveref}
\crefname{chapter}{Chapter}{Chapters}\Crefname{chapter}{Chapter}{Chapters}
\crefname{section}{Section}{Sections}\Crefname{section}{Section}{Sections}
\crefname{subsection}{Section}{Sections}\Crefname{subsection}{Section}{Sections}
\crefname{figure}{Figure}{Figures}\Crefname{figure}{Figure}{Figures}
\crefname{table}{Table}{Tables}\Crefname{table}{Table}{Tables}
\crefname{equation}{Equation}{Equations}\Crefname{equation}{Equation}{Equations}
\crefname{algorithm}{Algorithm}{Algorithms}\Crefname{algorithm}{Algorithm}{Algorithms}
\crefname{listing}{Listing}{Listings}\crefname{lstlisting}{Listing}{Listings}
\urlstyle{same}
\newcommand\creflastconjunction{ and }
\newcommand\creflastgroupconjunction{ and }

%% ---- Metadata -------------------------------------------------------------
\newcommand\fpt@set[2]{\csgdef{fpt@md@#1}{#2}}
\newcommand\fpt@get[1]{\ifcsdef{fpt@md@#1}{\csuse{fpt@md@#1}}{\TBC{#1}}}
\newcommand\ThesisSet[2]{\fpt@set{#1}{#2}}
\newcommand\ThesisGet[1]{\fpt@get{#1}}
\newcounter{fpt@members}
% \ThesisMember{full name}{roll number}{student code}
\newcommand\ThesisMember[3]{\stepcounter{fpt@members}%
  \csgdef{fpt@memberroll@\arabic{fpt@members}}{#2}%
  \csgdef{fpt@membercode@\arabic{fpt@members}}{#3}%
  \csgdef{fpt@membername@\arabic{fpt@members}}{#1}}
% value that the group still has to confirm: red in drafts, build error in final mode
\newcommand\TBC[1]{\ifthesisfinal
    \ClassError{fptthesis}{Unconfirmed value: #1}{Confirm it in config/metadata.tex.}%
  \else\texorpdfstring{\textcolor{fpttodo}{<#1>}}{<#1>}\fi}

%% ---- Writing aids (drafts only) -------------------------------------------
% \guide: instruction from a template; school style = blue italic. Hidden in final mode.
\newcommand\guide[1]{\ifthesisfinal\else{\color{fptguide}\itshape [#1]\par}\fi}
% \todo: open work; never allowed in a final build.
\newcommand\todo[1]{\ifthesisfinal
    \ClassError{fptthesis}{Open TODO: #1}{Resolve it before a submission build.}%
  \else{\color{fpttodo}\bfseries [TODO: #1]}\fi}

%% ---- Cover page 1: school (Template_AIP491), reproduced at measured positions
\RequirePackage{eso-pic}
\newlength\fpt@w
\newcommand\fpt@at[3]{\put(#1,-#2){\makebox(0,0)[lb]{\raisebox{0pt}[0pt][0pt]{#3}}}}
\newcommand\fpt@center[3]{\put(#1,-#2){\makebox[0pt]{\raisebox{0pt}[0pt][0pt]{#3}}}}
\newcommand\fpt@right[3]{\put(#1,-#2){\makebox[0pt][r]{\raisebox{0pt}[0pt][0pt]{#3}}}}
\newcommand\fpt@left[3]{\put(#1,-#2){\makebox[0pt][l]{\raisebox{0pt}[0pt][0pt]{#3}}}}
\newcommand\fpt@cal[2]{\fpt@calibri\fontsize{#1bp}{#1bp}\selectfont #2}
\newcommand\fpt@hline[3]{\put(#1,-#2){\rule{#3bp}{0.48bp}}}
\newcommand\fpt@vline[3]{\put(#1,-#2){\rule{0.48bp}{#3bp}}}
\newcommand\SchoolCover{%
  \clearpage\thispagestyle{empty}\null
  \begingroup\fpt@cal{11}{\fpt@measuremembers}\endgroup
  \AddToShipoutPictureBG*{\AtPageUpperLeft{\setlength\unitlength{1bp}%
    \begin{picture}(0,0)
      \fpt@left{97.72}{137.68}{\includegraphics[width=110.75bp,height=43.19bp]{\fpt@logoschool}}
      \fpt@left{251.3}{128.3}{\fpt@cal{16}{\bfseries MINISTRY OF EDUCATION AND TRAINING}}
      \fpt@center{298.3}{244.9}{\fpt@cal{36}{\bfseries FPT UNIVERSITY}}
      \fpt@center{302.25}{353.2}{\fpt@cambria\fontsize{28bp}{32bp}\selectfont Capstone Project Document}
      {\color{fptrule}\put(72,-379.6){\rule{452.6bp}{0.5bp}}}
      \put(72,-405.5){\parbox[t]{452.6bp}{\centering\parskip0pt\fpt@cambria\fontsize{22bp}{25.8bp}\selectfont \fpt@get{title}\par}}
      \fpt@hline{78.0}{453.1}{440.5}\fpt@hline{78.0}{497.6}{440.5}\fpt@hline{78.0}{586.05}{440.5}
      \fpt@hline{78.0}{611.0}{440.5}\fpt@hline{78.0}{636.0}{440.5}\fpt@hline{78.0}{660.95}{440.5}
      \fpt@vline{78.0}{660.95}{208.35}\fpt@vline{518.0}{660.95}{208.35}\fpt@vline{242.8}{660.95}{163.85}
      \fpt@center{298.3}{480.5}{\fpt@cal{18}{\bfseries\fpt@get{group}}}
      \fpt@right{237.6}{545.8}{\fpt@cal{14}{\bfseries Group Members}}
      \fpt@left{248.4}{514.0}{\fpt@cal{11}{\fpt@memberline{1}}}
      \fpt@left{248.4}{534.5}{\fpt@cal{11}{\fpt@memberline{2}}}
      \fpt@left{248.4}{554.9}{\fpt@cal{11}{\fpt@memberline{3}}}
      \fpt@left{248.4}{575.5}{\fpt@cal{11}{\fpt@memberline{4}}}
      \fpt@right{237.6}{602.5}{\fpt@cal{14}{\bfseries Supervisor}}
      \fpt@left{248.4}{602.5}{\fpt@cal{11}{\fpt@get{supervisor}}}
      \fpt@right{237.6}{627.5}{\fpt@cal{14}{\bfseries Ext Supervisor}}
      \fpt@left{248.4}{627.5}{\fpt@cal{11}{\fpt@get{extsupervisor}}}
      \fpt@right{237.6}{652.4}{\fpt@cal{14}{\bfseries Capstone Project code}}
      \fpt@left{248.4}{652.4}{\fpt@cal{11}{\fpt@get{projectcode}}}
      \fpt@center{307.05}{748.2}{\fpt@cal{14}{- Hanoi, \fpt@get{coverdate} -}}
    \end{picture}}}%
  \clearpage}
% members in three columns: name, roll number, student code (the template only has one line per member)
\newlength\fpt@namewd\newlength\fpt@rollwd
\newcommand\fpt@widest[2]{\settowidth\fpt@w{\csuse{#2}}\ifdim\fpt@w>#1\global#1=\fpt@w\fi}
\newcommand\fpt@measuremembers{%
  \@for\fpt@i:=1,2,3,4\do{%
    \fpt@widest\fpt@namewd{fpt@membername@\fpt@i}\fpt@widest\fpt@rollwd{fpt@memberroll@\fpt@i}}}
\newcommand\fpt@memberline[1]{\ifcsdef{fpt@membername@#1}{%
  \makebox[\fpt@namewd][l]{\csuse{fpt@membername@#1}}\hspace{16bp}%
  \makebox[\fpt@rollwd][l]{\csuse{fpt@memberroll@#1}}\hspace{16bp}\csuse{fpt@membercode@#1}}{}}
\newcommand\fpt@logoschool{logos/fpt-education.png}
\newcommand\fpt@logoteacher{logos/fpt-university.png}

%% ---- Cover page 2: supervisor's title page --------------------------------
\newcommand\fpt@memberlist{\ifcsdef{fpt@membername@1}{\csuse{fpt@membername@1}}{}%
  \ifcsdef{fpt@membername@2}{, \csuse{fpt@membername@2}}{}%
  \ifcsdef{fpt@membername@3}{,\penalty-50\space\csuse{fpt@membername@3}}{}%
  \ifcsdef{fpt@membername@4}{, \csuse{fpt@membername@4}}{}}
\newcommand\SupervisorTitlePage{%
  \clearpage\thispagestyle{empty}%
  \begingroup\parskip0pt\centering\setlength\topskip{18.8bp}%
  {\sffamily\bfseries\fpt@size{20}{23}\fpt@get{title}\par}%
  \fpt@gap[16.1bp]{53.2bp}{\sffamily\bfseries\fpt@size{14}{16.1}\fpt@get{reporttype}}%
  \fpt@gap[16.1bp]{40.1bp}{\sffamily\bfseries\fpt@size{14}{16.1}\ifcsdef{fpt@md@titleauthors}{\fpt@get{titleauthors}}{\fpt@memberlist}}%
  \fpt@gap{55.4bp}{\leftskip53.85bp plus 1fil\rightskip53.85bp plus 1fil\fpt@get{submission}}%
  \par\nointerlineskip\vspace{47.96bp}%
  {\includegraphics[width=297.25bp,height=66.15bp]{\fpt@logoteacher}\par}%
  \fpt@gap{126.6bp}{\fpt@get{degree}}%
  \fpt@gap{24.65bp}{\fpt@get{campus}}%
  \fpt@gap{24.65bp}{\fpt@get{date}}%
  \endgroup\clearpage}
% next paragraph's first baseline is exactly #1 below the previous baseline
\newcommand\fpt@gap[3][12.65bp]{\par\begingroup\lineskiplimit-\maxdimen
  \vskip\dimexpr#2-#1\relax{#3\par}\endgroup}

%% ---- Front-matter sections -------------------------------------------------
% \FrontSection[toc]{Title}: unnumbered H1 on a new page; * continues on the same page
% #1 = distance of the heading's baseline from the top of the text area
\newcommand\fpt@front@title[2][0bp]{{\fpt@hone\noindent\rule{0pt}{#1}#2\par}\nobreak\vskip0.95bp}
\NewDocumentCommand\FrontSection{s O{} m}{%
  \IfBooleanTF{#1}{\par\addvspace{16.95bp}}{\clearpage}%
  \phantomsection
  \ifstrequal{#2}{notoc}{\pdfbookmark[0]{#3}{front.#3}}{\addcontentsline{toc}{chapter}{#3}}%
  \IfBooleanTF{#1}{\fpt@front@title{#3}}{\fpt@front@title[33.02bp]{#3}}}
\NewDocumentCommand\FrontTop{m}{\clearpage\phantomsection\pdfbookmark[0]{#1}{front.#1}\fpt@front@title[15.02bp]{#1}}
\newcommand\TableOfContents{\FrontSection[notoc]{Table of Contents}\fpt@starttoc{toc}}
\newcommand\ListOfTables{\FrontSection*{List of tables}\fpt@starttoc{lot}}
\newcommand\ListOfFigures{\FrontSection*{List of figures}\fpt@starttoc{lof}}
\newcommand\fpt@starttoc[1]{\begingroup\parskip0pt\@starttoc{#1}\endgroup}
\newcommand\References{\chapter{References}\label{ch:references}\printbibliography[heading=none]}

% Acronym table (school: grid, shaded heading)
\newenvironment{acronymtable}{%
  \setlength\LTleft{0pt}\setlength\LTright{0pt}\setlength\LTpre{6bp}\setlength\LTpost{6bp}%
  \renewcommand\arraystretch{1.45}\parskip0pt
  \begin{longtable}{|>{\centering\arraybackslash}m{70.7bp-2\tabcolsep}|m{\dimexpr\textwidth-70.7bp-2\tabcolsep-3\arrayrulewidth}|}
  \hline\rowcolor{fpthead}\textbf{Acronym}&\multicolumn{1}{c|}{\cellcolor{fpthead}\textbf{Definition}}\\\hline\endhead
}{\end{longtable}}
\newcommand\acro[2]{#1 & #2\\\hline}

%% ---- Appendices -------------------------------------------------------------
\newcommand\Appendices{\chapter{Appendices}\label{ch:appendices}}

\AtBeginDocument{\hypersetup{pdftitle={\ThesisGet{title}},
  pdfsubject={Capstone Project Document, AIP491, FPT University},
  pdfkeywords={\ThesisGet{keywords}},pdfcreator={XeLaTeX; fptthesis v1.0},
  pdfauthor={\ThesisGet{group}; version \ThesisVersion; commit \ThesisCommit; \ThesisMode}}}
\endinput
