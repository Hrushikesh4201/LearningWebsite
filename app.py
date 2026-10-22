from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret"

QUIZZES = {
    "computer_fundamentals": [
        {
            "id": "q1",
            "unit": "Computer Fundamentals",
            "question": "A computer is an electronic device that accepts data, processes it, stores it and gives:",
            "options": ["Music", "Output", "Only games", "Only pictures"],
            "answer": 1,
            "explanation": "A computer takes input, processes it, and produces output."
        },
        {
            "id": "q2",
            "unit": "Computer Fundamentals",
            "question": "What is the correct order of computer working?",
            "options": [
                "Output → Process → Input",
                "Input → Process → Output",
                "Process → Storage → Input",
                "Storage → Output → Process"
            ],
            "answer": 1,
            "explanation": "Computers operate on the Input → Process → Output (IPO) cycle."
        },
        {
            "id": "q3",
            "unit": "Computer Fundamentals",
            "question": "Which generation of computers used Vacuum Tubes?",
            "options": ["First", "Second", "Third", "Fourth"],
            "answer": 0,
            "explanation": "First-generation computers used vacuum tubes for circuitry."
        },
        {
            "id": "q4",
            "unit": "Computer Fundamentals",
            "question": "Which of these is a characteristic of a computer?",
            "options": ["It gets tired", "High Speed", "It makes mistakes always", "It cannot store data"],
            "answer": 1,
            "explanation": "High speed and fast processing are key characteristics of computers."
        },
        {
            "id": "q5",
            "unit": "Computer Fundamentals",
            "question": "Which of these is an example of Hardware?",
            "options": ["MS Word", "Keyboard", "Google Chrome", "Windows"],
            "answer": 1,
            "explanation": "A keyboard is physical hardware that can be seen and touched."
        },
        {
            "id": "q6",
            "unit": "Computer Fundamentals",
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Control Power Unit"
            ],
            "answer": 0,
            "explanation": "CPU stands for Central Processing Unit."
        },
        {
            "id": "q7",
            "unit": "Computer Fundamentals",
            "question": "RAM is a type of:",
            "options": ["Permanent memory", "Temporary memory", "Output device", "Input device"],
            "answer": 1,
            "explanation": "RAM is volatile, temporary memory."
        },
        {
            "id": "q8",
            "unit": "Computer Fundamentals",
            "question": "Which of these is Application Software?",
            "options": ["Windows", "Linux", "MS Word", "All of the above"],
            "answer": 2,
            "explanation": "MS Word is application software used for word processing, while Windows and Linux are operating systems."
        },
        {
            "id": "q9",
            "unit": "Computer Fundamentals",
            "question": "Why is a computer called “diligent”?",
            "options": [
                "It works very slowly",
                "It does not get tired",
                "It needs rest every hour",
                "It only works in the morning"
            ],
            "answer": 1,
            "explanation": "Diligence means the computer can perform repetitive tasks without getting tired or losing concentration."
        },
        {
            "id": "q10",
            "unit": "Computer Fundamentals",
            "question": "Which of the following is a disadvantage of computers?",
            "options": ["High Speed", "Large Storage", "Cyber Security Risks", "Accuracy"],
            "answer": 2,
            "explanation": "Cyber security risks and vulnerability to viruses are disadvantages of using computers."
        }
    ],


    "operating_system": [
        {
            "id": "q1",
            "unit": "Operating System and File Management",
            "question": "An Operating System acts as a bridge between:",
            "options": [
                "User and the computer",
                "Two computers",
                "Printer and mouse",
                "Only keyboard and monitor"
            ],
            "answer": 0,
            "explanation": "An OS provides an interface between the user/software and the hardware."
        },
        {
            "id": "q2",
            "unit": "Operating System and File Management",
            "question": "Which of these is a Desktop Operating System?",
            "options": ["Android", "Windows", "iOS", "Only mobile phones"],
            "answer": 1,
            "explanation": "Windows is a desktop/laptop operating system, while Android and iOS are mobile operating systems."
        },
        {
            "id": "q3",
            "unit": "Operating System and File Management",
            "question": "What do we use to organize files?",
            "options": ["Only Desktop", "Folders", "Only Recycle Bin", "Only Taskbar"],
            "answer": 1,
            "explanation": "Folders are used to group and organize related files."
        },
        {
            "id": "q4",
            "unit": "Operating System and File Management",
            "question": "Which shortcut is used to Copy a file?",
            "options": ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"],
            "answer": 1,
            "explanation": "Ctrl + C copies the selected file or item."
        },
        {
            "id": "q5",
            "unit": "Operating System and File Management",
            "question": "When we delete a file, it first goes to:",
            "options": ["Documents", "Recycle Bin", "Desktop", "It is permanently deleted"],
            "answer": 1,
            "explanation": "Deleted files are moved to the Recycle Bin before permanent deletion."
        },
        {
            "id": "q6",
            "unit": "Operating System and File Management",
            "question": "Which file extension is used for a Word document?",
            "options": [".xlsx", ".docx", ".pptx", ".jpg"],
            "answer": 1,
            "explanation": ".docx is the standard file extension for Microsoft Word documents."
        },
        {
            "id": "q7",
            "unit": "Operating System and File Management",
            "question": "What does the Taskbar show?",
            "options": [
                "Only the background",
                "Open apps and system clock",
                "Only files",
                "Only folders"
            ],
            "answer": 1,
            "explanation": "The Taskbar displays currently active applications, pinned programs, and the system tray/clock."
        },
        {
            "id": "q8",
            "unit": "Operating System and File Management",
            "question": "How can we rename a file quickly?",
            "options": ["Press F2", "Press Ctrl + S", "Press Delete", "Press Ctrl + C"],
            "answer": 0,
            "explanation": "F2 is the keyboard shortcut to rename a selected file or folder."
        },
        {
            "id": "q9",
            "unit": "Operating System and File Management",
            "question": "Why should we use clear names for folders (example: Project_Report_v1)?",
            "options": [
                "To make the computer faster",
                "To easily find and understand files later",
                "To increase file size",
                "It is not important"
            ],
            "answer": 1,
            "explanation": "Descriptive naming allows quick locating and understanding of contents."
        },
        {
            "id": "q10",
            "unit": "Operating System and File Management",
            "question": "What is the correct way to create a new folder on the desktop?",
            "options": [
                "Right-click → New → Folder",
                "Press Ctrl + S",
                "Open Recycle Bin",
                "Press Delete"
            ],
            "answer": 0,
            "explanation": "Right-clicking an empty space and selecting New → Folder creates a folder."
        }
    ],


    "website_creation": [
        {
            "id": "q1",
            "unit": "Website Creation (Wix)",
            "question": "A website is a collection of:",
            "options": ["Only pictures", "Linked pages", "Only videos", "Only games"],
            "answer": 1,
            "explanation": "A website consists of connected, interlinked web pages."
        },
        {
            "id": "q2",
            "unit": "Website Creation (Wix)",
            "question": "Wix is a:",
            "options": [
                "Programming language",
                "Drag-and-drop website builder",
                "Type of computer",
                "Operating system"
            ],
            "answer": 1,
            "explanation": "Wix is a visual drag-and-drop platform for designing and building websites."
        },
        {
            "id": "q3",
            "unit": "Website Creation (Wix)",
            "question": "What is the main landing page of a website called?",
            "options": ["About page", "Homepage", "Contact page", "Gallery"],
            "answer": 1,
            "explanation": "The main starting/default page is known as the Homepage."
        },
        {
            "id": "q4",
            "unit": "Website Creation (Wix)",
            "question": "Which element is used to display photos on a website?",
            "options": ["Text Box", "Image", "Button", "Link"],
            "answer": 1,
            "explanation": "Image elements display photographs and graphics."
        },
        {
            "id": "q5",
            "unit": "Website Creation (Wix)",
            "question": "What should we do before publishing a website?",
            "options": [
                "Delete all pages",
                "Preview it on desktop and mobile",
                "Remove all images",
                "Change the name every time"
            ],
            "answer": 1,
            "explanation": "Previewing ensures layout and formatting look correct on both mobile and desktop screens."
        },
        {
            "id": "q6",
            "unit": "Website Creation (Wix)",
            "question": "What is the purpose of a Button on a website?",
            "options": [
                "Only to show text",
                "To trigger an action (like going to another page)",
                "Only for decoration",
                "To play music only"
            ],
            "answer": 1,
            "explanation": "Buttons provide interactive calls to action, such as navigation or form submission."
        },
        {
            "id": "q7",
            "unit": "Website Creation (Wix)",
            "question": "Which of these is a good design principle?",
            "options": [
                "Use many different fonts and colours randomly",
                "Keep layout clean and use consistent colours",
                "Put very small text",
                "Fill every space with text"
            ],
            "answer": 1,
            "explanation": "Clean layouts with consistent color schemes create professional, readable pages."
        },
        {
            "id": "q8",
            "unit": "Website Creation (Wix)",
            "question": "What does “Publish” mean in Wix?",
            "options": [
                "Delete the website",
                "Make the website live on the internet",
                "Only save it",
                "Change the template"
            ],
            "answer": 1,
            "explanation": "Publishing pushes your draft online for visitors to access via URL."
        },
        {
            "id": "q9",
            "unit": "Website Creation (Wix)",
            "question": "Why is it important to have a Navigation menu?",
            "options": [
                "To make the website look colourful",
                "So visitors can easily move between pages",
                "To increase the size of the website",
                "It is not needed"
            ],
            "answer": 1,
            "explanation": "Navigation bars help visitors locate and browse between website pages easily."
        },
        {
            "id": "q10",
            "unit": "Website Creation (Wix)",
            "question": "In the final project, students must create at least how many pages?",
            "options": [
                "One page",
                "Two pages",
                "Three pages (Home, About, Contact)",
                "Ten pages"
            ],
            "answer": 2,
            "explanation": "A standard beginner web project comprises three core pages: Home, About, and Contact."
        }
    ],

    "introduction_to_coding": [
        {
            "id": "q1",
            "unit": "Introduction to Coding",
            "question": "Coding means writing:",
            "options": [
                "Stories",
                "Instructions for the computer",
                "Only drawings",
                "Only songs"
            ],
            "answer": 1,
            "explanation": "Coding is writing instructions that tell a computer what to execute."
        },
        {
            "id": "q2",
            "unit": "Introduction to Coding",
            "question": "Breaking a big problem into smaller parts is called:",
            "options": ["Abstraction", "Decomposition", "Pattern Recognition", "Algorithm"],
            "answer": 1,
            "explanation": "Decomposition breaks complex problems down into smaller, manageable chunks."
        },
        {
            "id": "q3",
            "unit": "Introduction to Coding",
            "question": "An algorithm is:",
            "options": [
                "A type of computer",
                "A sequence of steps to solve a problem",
                "A virus",
                "A website"
            ],
            "answer": 1,
            "explanation": "An algorithm is an ordered set of instructions designed to achieve an outcome."
        },
        {
            "id": "q4",
            "unit": "Introduction to Coding",
            "question": "In a flowchart, which symbol is used for Start and End?",
            "options": ["Rectangle", "Diamond", "Oval", "Arrow"],
            "answer": 2,
            "explanation": "Ovals (terminators) denote the Start and End of a flowchart process."
        },
        {
            "id": "q5",
            "unit": "Introduction to Coding",
            "question": "Scratch is good for beginners because it uses:",
            "options": [
                "Only text code",
                "Drag-and-drop blocks",
                "Only hardware",
                "Only pictures"
            ],
            "answer": 1,
            "explanation": "Scratch uses visual, snap-together blocks to teach computational thinking without syntax errors."
        },
        {
            "id": "q6",
            "unit": "Introduction to Coding",
            "question": "What is used to store data like numbers or text in a program?",
            "options": ["Loop", "Variable", "Event", "Sprite"],
            "answer": 1,
            "explanation": "Variables act as named containers for storing and updating values in code."
        },
        {
            "id": "q7",
            "unit": "Introduction to Coding",
            "question": "What do loops do in coding?",
            "options": ["Store data", "Repeat actions many times", "Make decisions", "Delete code"],
            "answer": 1,
            "explanation": "Loops automate repeated execution of code blocks."
        },
        {
            "id": "q8",
            "unit": "Introduction to Coding",
            "question": "Which symbol in a flowchart is used for Yes/No decisions?",
            "options": ["Oval", "Rectangle", "Diamond", "Arrow"],
            "answer": 2,
            "explanation": "A diamond represents a conditional decision point with branching paths."
        },
        {
            "id": "q9",
            "unit": "Introduction to Coding",
            "question": "Why do we make a flowchart before writing code?",
            "options": [
                "To make the program colourful",
                "To plan the logic step by step",
                "To increase the size of the program",
                "It is not useful"
            ],
            "answer": 1,
            "explanation": "Flowcharts help visualize and plan the algorithm's control flow before coding begins."
        },
        {
            "id": "q10",
            "unit": "Introduction to Coding",
            "question": "What should you do after building a program?",
            "options": [
                "Never test it",
                "Test it and fix errors (debugging)",
                "Delete it immediately",
                "Only show it without testing"
            ],
            "answer": 1,
            "explanation": "Testing and debugging verify that code functions correctly and handles edge cases."
        }
    ],

    "ms_word": [
        {
            "id": "q1",
            "unit": "Microsoft Word",
            "question": "Microsoft Word is used to create:",
            "options": ["Only pictures", "Text documents", "Only videos", "Only spreadsheets"],
            "answer": 1,
            "explanation": "MS Word is a word processor designed for creating text-based documents."
        },
        {
            "id": "q2",
            "unit": "Microsoft Word",
            "question": "Which shortcut is used to make text Bold?",
            "options": ["Ctrl + I", "Ctrl + B", "Ctrl + U", "Ctrl + S"],
            "answer": 1,
            "explanation": "Ctrl + B applies bold weight to selected text."
        },
        {
            "id": "q3",
            "unit": "Microsoft Word",
            "question": "Which shortcut is used to Save a document?",
            "options": ["Ctrl + P", "Ctrl + S", "Ctrl + Z", "Ctrl + C"],
            "answer": 1,
            "explanation": "Ctrl + S saves the current document file."
        },
        {
            "id": "q4",
            "unit": "Microsoft Word",
            "question": "What is used to make a list of points without numbers?",
            "options": ["Numbering", "Bullets", "Table", "Header"],
            "answer": 1,
            "explanation": "Bullet points create unordered lists."
        },
        {
            "id": "q5",
            "unit": "Microsoft Word",
            "question": "Which shortcut is used to Undo a mistake?",
            "options": ["Ctrl + Y", "Ctrl + Z", "Ctrl + S", "Ctrl + P"],
            "answer": 1,
            "explanation": "Ctrl + Z reverts the last action."
        },
        {
            "id": "q6",
            "unit": "Microsoft Word",
            "question": "Where do we go to insert a picture?",
            "options": ["Home tab", "Insert → Pictures", "Design tab", "Layout tab"],
            "answer": 1,
            "explanation": "Images are placed from the Insert tab via the Pictures button."
        },
        {
            "id": "q7",
            "unit": "Microsoft Word",
            "question": "What is the purpose of Headers and Footers?",
            "options": [
                "To change font colour",
                "To add page numbers or title on every page",
                "To insert tables",
                "To make text bold"
            ],
            "answer": 1,
            "explanation": "Headers and footers repeat elements like titles, authors, and page numbers across pages."
        },
        {
            "id": "q8",
            "unit": "Microsoft Word",
            "question": "Which alignment makes text look even on both left and right sides?",
            "options": ["Left", "Center", "Right", "Justify"],
            "answer": 3,
            "explanation": "Justify alignment spaces text evenly between left and right margins."
        },
        {
            "id": "q9",
            "unit": "Microsoft Word",
            "question": "Why is it important to use consistent fonts and headings?",
            "options": [
                "To make the document look professional and easy to read",
                "To increase the file size",
                "It is not important",
                "Only for colour"
            ],
            "answer": 0,
            "explanation": "Consistent typography enhances readability and visual hierarchy."
        },
        {
            "id": "q10",
            "unit": "Microsoft Word",
            "question": "In the final project, students must create a one-page:",
            "options": ["Only table", "Resume or event flyer", "Only picture", "Only list"],
            "answer": 1,
            "explanation": "A one-page resume or event flyer practices formatting, layout, and styling skills."
        }
    ],

    "ms_powerpoint": [
        {
            "id": "q1",
            "unit": "Microsoft PowerPoint",
            "question": "A single screen in a presentation is called a:",
            "options": ["Workbook", "Slide", "Cell", "Folder"],
            "answer": 1,
            "explanation": "Each individual screen or canvas in PowerPoint is called a slide."
        },
        {
            "id": "q2",
            "unit": "Microsoft PowerPoint",
            "question": "What is used to add a new slide?",
            "options": ["Design tab", "New Slide button", "Animations tab", "Transitions tab"],
            "answer": 1,
            "explanation": "The New Slide button (in the Home or Insert tab) appends an additional slide."
        },
        {
            "id": "q3",
            "unit": "Microsoft PowerPoint",
            "question": "Animations control how elements appear:",
            "options": ["Between slides", "On a single slide", "Only on the title", "Only when printing"],
            "answer": 1,
            "explanation": "Animations apply entrance, emphasis, or exit effects to individual items on a slide."
        },
        {
            "id": "q4",
            "unit": "Microsoft PowerPoint",
            "question": "Transitions control how:",
            "options": [
                "Text becomes bold",
                "One slide changes to the next",
                "Pictures are inserted",
                "Font size changes"
            ],
            "answer": 1,
            "explanation": "Transitions control the motion effect when advancing from one slide to another."
        },
        {
            "id": "q5",
            "unit": "Microsoft PowerPoint",
            "question": "What is the best way to use text on slides?",
            "options": [
                "Write long paragraphs",
                "Use short bullet points",
                "Fill the whole slide with text",
                "Use very small font"
            ],
            "answer": 1,
            "explanation": "Concise bullet points allow the audience to read quickly without distraction."
        },
        {
            "id": "q6",
            "unit": "Microsoft PowerPoint",
            "question": "Why should we use animations and transitions carefully?",
            "options": [
                "To make the presentation longer",
                "So that they do not distract the audience",
                "To increase file size",
                "They are not useful"
            ],
            "answer": 1,
            "explanation": "Overusing effects can distract from the core message and presentation content."
        },
        {
            "id": "q7",
            "unit": "Microsoft PowerPoint",
            "question": "What is Slide Show mode?",
            "options": [
                "Editing mode",
                "Full-screen presentation view",
                "Only printing mode",
                "Only notes view"
            ],
            "answer": 1,
            "explanation": "Slide Show mode displays slides in full screen for presenting to an audience."
        },
        {
            "id": "q8",
            "unit": "Microsoft PowerPoint",
            "question": "In a group presentation, students should:",
            "options": [
                "Read every word from the slide",
                "Maintain eye contact and speak clearly",
                "Look only at the screen",
                "Speak very fast"
            ],
            "answer": 1,
            "explanation": "Effective speakers engage their audience with eye contact and clear pacing."
        },
        {
            "id": "q9",
            "unit": "Microsoft PowerPoint",
            "question": "Why should slides support the speaker and not replace them?",
            "options": [
                "Because slides are only for decoration",
                "Because the speaker explains the points, slides show key ideas",
                "Because text is not important",
                "It is not a good practice"
            ],
            "answer": 1,
            "explanation": "Slides act as visual cues, while the speaker provides context and explanation."
        },
        {
            "id": "q10",
            "unit": "Microsoft PowerPoint",
            "question": "In the final project, the presentation should have:",
            "options": [
                "Only 1 slide",
                "5–7 slides with title, content and summary",
                "Only pictures",
                "Only animations"
            ],
            "answer": 1,
            "explanation": "5–7 slides provide sufficient structure for an introduction, body, and conclusion."
        }
    ],

    "ms_excel": [
        {
            "id": "q1",
            "unit": "Microsoft Excel",
            "question": "In Excel, the meeting point of a row and a column is called a:",
            "options": ["Workbook", "Worksheet", "Cell", "Chart"],
            "answer": 2,
            "explanation": "A cell is the single unit formed where a row and column intersect."
        },
        {
            "id": "q2",
            "unit": "Microsoft Excel",
            "question": "Formulas in Excel always begin with:",
            "options": ["#", "=", "@", "$"],
            "answer": 1,
            "explanation": "All formulas and calculations in Excel start with an equal sign (=)."
        },
        {
            "id": "q3",
            "unit": "Microsoft Excel",
            "question": "Which formula adds the values in A1 and A2?",
            "options": ["=A1-A2", "=A1+A2", "=A1*A2", "=A1/A2"],
            "answer": 1,
            "explanation": "=A1+A2 adds cell A1 to cell A2."
        },
        {
            "id": "q4",
            "unit": "Microsoft Excel",
            "question": "Which function is used to add many numbers quickly?",
            "options": ["=AVERAGE", "=SUM", "=MAX", "=MIN"],
            "answer": 1,
            "explanation": "=SUM() quickly totals contiguous or multiple cell ranges."
        },
        {
            "id": "q5",
            "unit": "Microsoft Excel",
            "question": "Rows in Excel are numbered and columns are:",
            "options": ["Also numbered", "Lettered (A, B, C...)", "Both numbered", "Not marked"],
            "answer": 1,
            "explanation": "Rows are identified by numbers (1, 2, 3...) and columns by letters (A, B, C...)."
        },
        {
            "id": "q6",
            "unit": "Microsoft Excel",
            "question": "What does the function =AVERAGE(A1:A10) do?",
            "options": [
                "Adds the numbers",
                "Finds the mean (average) value",
                "Finds the highest value",
                "Finds the lowest value"
            ],
            "answer": 1,
            "explanation": "The AVERAGE function calculates the arithmetic mean of the given cells."
        },
        {
            "id": "q7",
            "unit": "Microsoft Excel",
            "question": "What is Freezing Panes used for?",
            "options": [
                "To delete rows",
                "To keep headers visible while scrolling",
                "To change colour",
                "To make charts"
            ],
            "answer": 1,
            "explanation": "Freeze Panes locks rows or columns in view as you scroll through large sheets."
        },
        {
            "id": "q8",
            "unit": "Microsoft Excel",
            "question": "Which feature helps us see only the rows we want?",
            "options": ["Sort", "Filter", "Chart", "Freeze Panes"],
            "answer": 1,
            "explanation": "Filtering temporarily hides rows that do not match specified criteria."
        },
        {
            "id": "q9",
            "unit": "Microsoft Excel",
            "question": "Why do we use charts in Excel?",
            "options": [
                "To make the file larger",
                "To visualize data so it is easier to understand",
                "Only for decoration",
                "Charts are not useful"
            ],
            "answer": 1,
            "explanation": "Charts convert numeric tables into graphics for quick analysis and comparisons."
        },
        {
            "id": "q10",
            "unit": "Microsoft Excel",
            "question": "In the practical project, students must create a spreadsheet for:",
            "options": [
                "Only names",
                "Weekly expenses and use SUM, AVERAGE and a pie chart",
                "Only pictures",
                "Only text"
            ],
            "answer": 1,
            "explanation": "Tracking weekly expenses applies math functions like SUM, AVERAGE, and visual charting."
        }
    ]
}

# Aliases matching course URL endpoints
QUIZZES["osandfm"] = QUIZZES["operating_system"]
QUIZZES["mssheets"] = QUIZZES["ms_excel"]
QUIZZES["introtocoding"] = QUIZZES["introduction_to_coding"]
QUIZZES["mspowerpoint"] = QUIZZES["ms_powerpoint"]
QUIZZES["msword"] = QUIZZES["ms_word"]



PRACTICE = {
    "computer_fundamentals": {
        "Computer Fundamentals": [
            {"question": "What is a computer?", "answer": "An electronic device that accepts data (input), processes it, stores it, and delivers output.", "explanation": "A computer performs input, processing, storage and output operations."},
            {"question": "What is the standard cycle of computer operation?", "answer": "Input → Process → Output (IPO) cycle.", "explanation": "Data enters as input, is processed and produces output."},
            {"question": "Which hardware technology powered first-generation computers?", "answer": "Vacuum tubes.", "explanation": "First-generation computers used vacuum tubes for electronic circuitry."},
            {"question": "What is a key defining characteristic of computers compared to humans?", "answer": "High operating speed, accuracy and diligence without fatigue.", "explanation": "Computers can perform repetitive operations quickly and consistently."},
            {"question": "What is computer hardware?", "answer": "The physical parts of a computer, such as the keyboard, mouse and monitor.", "explanation": "Hardware refers to the tangible components of a computer system."},
            {"question": "What does CPU stand for?", "answer": "Central Processing Unit, often called the brain of the computer.", "explanation": "The CPU executes instructions and processes data."},
            {"question": "What type of memory is RAM?", "answer": "Volatile, temporary memory that loses its contents when power is turned off.", "explanation": "RAM temporarily holds data and instructions in use."},
            {"question": "What is application software?", "answer": "Programs designed to help users perform specific tasks, such as Microsoft Word or web browsers.", "explanation": "Application software helps users complete particular activities."},
            {"question": 'Why is a computer considered "diligent"?', "answer": "It can perform repetitive tasks continuously without getting tired or losing accuracy.", "explanation": "Computers do not experience physical fatigue when repeating tasks."},
            {"question": "What is a major disadvantage of using computers?", "answer": "Vulnerability to cybersecurity threats, viruses and data breaches.", "explanation": "Security controls are needed to protect computer systems and information."}
        ]
    },

"operating_system": {
    "Operating System and File Management": [
            {"question": "What is an Operating System (OS)?", "answer": "System software that acts as an interface between the user and the computer hardware.", "explanation": "An OS manages hardware resources and provides services for applications."},
            {"question": "Name a common desktop operating system.", "answer": "Microsoft Windows, macOS or Linux.", "explanation": "These operating systems are used on desktop and laptop computers."},
            {"question": "What is the primary tool used to organize files on a computer?", "answer": "Folders (directories).", "explanation": "Folders group files and help organize information."},
            {"question": "Which shortcut key is used to copy a selected file or folder?", "answer": "Ctrl + C.", "explanation": "Ctrl + C copies the selected item."},
            {"question": "Where does a deleted file go before permanent removal in Windows?", "answer": "The Recycle Bin, when it is a normal deletion.", "explanation": "Files deleted normally can often be restored from the Recycle Bin."},
            {"question": "What file extension identifies a modern Microsoft Word document?", "answer": ".docx.", "explanation": "The .docx extension is used for modern Word documents."},
            {"question": "What is the purpose of the Windows Taskbar?", "answer": "To display open applications, pinned shortcuts and the system clock.", "explanation": "The Taskbar provides quick access to applications and system information."},
            {"question": "Which keyboard shortcut allows you to quickly rename a file in Windows?", "answer": "F2.", "explanation": "Select a file and press F2 to rename it."},
            {"question": "Why should you use descriptive names when saving folders and files?", "answer": "To make documents easy to search, identify and retrieve later.", "explanation": "Meaningful names make file organization easier."},
            {"question": "How do you create a new folder on the desktop using a mouse?", "answer": "Right-click empty space, select New, and click Folder.", "explanation": "This is the standard Windows desktop method for creating a folder."}
        ]
    },

    "website_creation": {
        "Website Creation (Wix)" :[
            {"question": "What is a website?", "answer": "A collection of publicly accessible, interlinked web pages sharing a single domain name.", "explanation": "Websites commonly contain multiple related pages accessible through a browser."},
            {"question": "What kind of tool is Wix?", "answer": "A visual, drag-and-drop cloud-based website builder that requires no coding.", "explanation": "Wix lets users create websites using a visual editor."},
            {"question": "What is the primary landing page of a website called?", "answer": "The Homepage.", "explanation": "The homepage is usually the main entry point to a website."},
            {"question": "Which Wix element is added to show graphics and photos?", "answer": "The Image element.", "explanation": "An image element displays pictures and graphics on a page."},
            {"question": "Why should you preview a site before publishing?", "answer": "To verify formatting, layouts and links on desktop and mobile screens.", "explanation": "Previewing helps identify layout and navigation issues before publishing."},
            {"question": "What is the function of a website button?", "answer": "To trigger an action when clicked, such as opening a page or submitting a form.", "explanation": "Buttons let visitors perform actions on a website."},
            {"question": "What is a fundamental principle of good web design?", "answer": "Keeping layouts clean and uncluttered, with consistent colors and typography.", "explanation": "Consistency makes a website easier to use and read."},
            {"question": 'What does the "Publish" button do in Wix?', "answer": "It makes saved site changes live and accessible to visitors on the internet.", "explanation": "Publishing makes the website available to its intended audience."},
            {"question": "Why is a navigation menu essential on a website?", "answer": "It lets visitors move smoothly between different pages.", "explanation": "Navigation helps users find the content they need."},
            {"question": "What are three standard core pages in a beginner website project?", "answer": "Home, About and Contact pages.", "explanation": "These pages introduce the site, explain its purpose and provide contact information."}
        ]
    },

    "introduction_to_coding": {
        "Introduction to Coding": [
            {"question": "What is coding?", "answer": "Writing step-by-step instructions in a programming language that a computer can execute.", "explanation": "Code tells a computer what operations to perform."},
            {"question": "What does decomposition mean in computational thinking?", "answer": "Breaking a complex problem into smaller, simpler and more manageable parts.", "explanation": "Smaller problems are easier to understand and solve."},
            {"question": "What is an algorithm?", "answer": "A clear, step-by-step set of ordered rules designed to solve a specific problem.", "explanation": "An algorithm defines the steps needed to solve a problem."},
            {"question": "Which flowchart symbol represents the Start and End points?", "answer": "An oval, also called a terminator.", "explanation": "An oval marks the beginning or end of a flowchart."},
            {"question": "Why is Scratch widely recommended for beginner programmers?", "answer": "It uses visual, snap-together graphical blocks to teach logic without syntax errors.", "explanation": "Block-based coding helps beginners focus on programming concepts."},
            {"question": "What is a variable used for in programming?", "answer": "A named storage container used to hold data values, such as numbers or text, that can change.", "explanation": "Variables allow programs to store and use information."},
            {"question": "What is the role of a loop in programming?", "answer": "To repeat a block of instructions multiple times automatically until a condition is met.", "explanation": "Loops reduce the need to write the same instructions repeatedly."},
            {"question": "Which flowchart symbol represents a decision or condition (Yes/No)?", "answer": "A diamond.", "explanation": "A diamond represents a decision that branches according to a condition."},
            {"question": "Why create a flowchart or pseudocode before coding?", "answer": "To map out and verify program logic before writing actual code.", "explanation": "Planning helps identify logical problems before implementation."},
            {"question": "What is debugging?", "answer": "The process of testing a program to find and fix errors or unexpected behavior.", "explanation": "Debugging helps a program work as intended."}
        ]
    },

    "ms_word": {
        "Microsoft Word": [
            {"question": "What is Microsoft Word primarily used for?", "answer": "Creating, editing, formatting and printing text-based documents.", "explanation": "Word is a word-processing application."},
            {"question": "Which shortcut key applies Bold styling to selected text?", "answer": "Ctrl + B.", "explanation": "Ctrl + B toggles bold formatting."},
            {"question": "Which keyboard shortcut saves the active document?", "answer": "Ctrl + S.", "explanation": "Ctrl + S saves the current document."},
            {"question": "What formatting tool organizes points into a list without numbers?", "answer": "Bullet points.", "explanation": "Bullets create an unordered list."},
            {"question": "Which keyboard shortcut reverses the most recent mistake (Undo)?", "answer": "Ctrl + Z.", "explanation": "Undo reverses the most recent supported action."},
            {"question": "Where on the Word ribbon do you find the option to add images?", "answer": "The Insert tab under the Pictures group.", "explanation": "The Insert tab provides options for adding pictures and other elements."},
            {"question": "What is the purpose of headers and footers?", "answer": "To display repeated information, such as page numbers and document titles, at the top or bottom of pages.", "explanation": "Headers and footers provide consistent page information."},
            {"question": "Which text alignment spaces words evenly between both left and right margins?", "answer": "Justify alignment (Ctrl + J).", "explanation": "Justified text aligns with both margins, except where the final line is handled differently."},
            {"question": "Why is consistent font styling and hierarchy important?", "answer": "It makes documents structured, professional and easier to read.", "explanation": "Consistent formatting helps readers understand document organization."},
            {"question": "What project best demonstrates beginner MS Word layout skills?", "answer": "A clean, one-page personal resume or an event flyer.", "explanation": "These projects demonstrate text formatting, alignment and page layout."}
        ]
    },

    "ms_powerpoint": {
        "Microsoft PowerPoint": [
            {"question": "What is an individual page or display screen in PowerPoint called?", "answer": "A slide.", "explanation": "A presentation is made up of individual slides."},
            {"question": "How do you insert an additional slide into your presentation?", "answer": "Click the New Slide button on the Home or Insert tab.", "explanation": "The New Slide command adds another slide to the presentation."},
            {"question": "What do animations apply to in PowerPoint?", "answer": "Specific text boxes, images or other elements on an individual slide.", "explanation": "Animations control how individual slide objects appear or move."},
            {"question": "What do transitions apply to in PowerPoint?", "answer": "The visual motion effect seen when switching from one slide to the next.", "explanation": "Transitions control the change between slides."},
            {"question": "What is the best rule for displaying text on presentation slides?", "answer": "Use short, concise bullet points rather than lengthy paragraphs.", "explanation": "Brief text is easier for an audience to follow."},
            {"question": "Why should you keep slide animations and transitions minimal?", "answer": "To maintain audience focus on the presentation topic rather than visual distractions.", "explanation": "Subtle effects help keep attention on the content."},
            {"question": "What is Slide Show mode?", "answer": "A full-screen view used to display the presentation to an audience.", "explanation": "Slide Show mode presents slides in presentation format."},
            {"question": "What is a key speaking habit during a live slide presentation?", "answer": "Make regular eye contact and speak clearly rather than reading directly from the screen.", "explanation": "Eye contact and clear speech help engage the audience."},
            {"question": "What is the true purpose of presentation slides?", "answer": "To visually support and reinforce the speaker's main points, not replace the speaker.", "explanation": "Slides complement the speaker's explanation."},
            {"question": "What is a recommended slide count for a beginner presentation project?", "answer": "Five to seven structured slides covering an introduction, main points and a summary.", "explanation": "A short presentation helps beginners practice organizing information."}
        ]
    },

    "ms_excel": {
        "Microsoft Excel": [
            {"question": "What is a cell in Microsoft Excel?", "answer": "The rectangular intersection where a specific row and column meet.", "explanation": "A cell is identified by its column letter and row number."},
            {"question": "What character must precede every formula or function in Excel?", "answer": "The equal sign (=).", "explanation": "Excel formulas normally begin with an equal sign."},
            {"question": "What basic formula adds the values stored in cells A1 and A2?", "answer": "=A1+A2.", "explanation": "The plus operator adds the values of the two referenced cells."},
            {"question": "Which built-in function calculates the total of a range of numbers?", "answer": "The =SUM() function.", "explanation": "SUM adds numerical values in a range."},
            {"question": "How are rows and columns labeled in an Excel spreadsheet?", "answer": "Rows use numbers (1, 2, 3...) and columns use letters (A, B, C...).", "explanation": "Cell addresses combine a column letter and row number."},
            {"question": "What does =AVERAGE(A1:A10) calculate?", "answer": "The arithmetic mean of numeric values in cells A1 through A10.", "explanation": "AVERAGE calculates the mean of the numerical values in the range."},
            {"question": "Why use Freeze Panes in Excel?", "answer": "To keep selected header rows or columns visible while scrolling through a dataset.", "explanation": "Freeze Panes helps retain context in large worksheets."},
            {"question": "What does the Filter tool do in a spreadsheet?", "answer": "It temporarily hides rows that do not meet selected criteria while keeping matching data visible.", "explanation": "Filtering displays the rows that meet chosen conditions."},
            {"question": "Why are visual charts used in spreadsheets?", "answer": "To turn raw numerical data into easy-to-understand visual trends and patterns.", "explanation": "Charts make comparisons and trends easier to interpret."},
            {"question": "What is a practical project for practicing basic Excel formulas and charts?", "answer": "A weekly budget tracker using SUM, AVERAGE and a pie or bar chart.", "explanation": "A budget tracker provides practice with formulas and data visualization."}
        ]
    }
}

# Aliases matching course URL endpoints
PRACTICE["osandfm"] = PRACTICE["operating_system"]
PRACTICE["mssheets"] = PRACTICE["ms_excel"]
PRACTICE["introtocoding"] = PRACTICE["introduction_to_coding"]
PRACTICE["mspowerpoint"] = PRACTICE["ms_powerpoint"]
PRACTICE["msword"] = PRACTICE["ms_word"]
# Process submitted answers and calculate score
@app.route("/quiz/<course>/submit", methods=["POST"])
def submit_quiz(course):
    questions = QUIZZES.get(course)

    if questions is None:
        return "Course not found", 404

    correct_count = 0
    wrong_units = set()
    results = []

    for q in questions:
        selected = request.form.get(q["id"])

        # Validate the submitted option index
        valid_selection = (
            selected is not None
            and selected.isdigit()
            and 0 <= int(selected) < len(q["options"])
        )

        is_correct = (
            valid_selection
            and int(selected) == q["answer"]
        )

        if is_correct:
            correct_count += 1
        else:
            wrong_units.add(q["unit"])

        results.append({
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["answer"],
            "selected": int(selected) if valid_selection else None,
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })

    total = len(questions)
    percentage = correct_count / total * 100 if total else 0

    # Keep the latest result for this course in the session
    session[f"quiz_{course}"] = {
        "percentage": percentage,
        "wrong_units": sorted(wrong_units)
    }

    return render_template(
        "quiz_result.html",
        course=course,
        score=correct_count,
        total=total,
        percentage=percentage,
        results=results,
        needs_practice=percentage < 40,
        passed=percentage >= 40
    )



# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Courses Page
@app.route("/courses")
def courses():
    return render_template("courses.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/computer_fundamentals")
def computer_fundamentals():
    return render_template("computer_fundamentals.html")


@app.route("/OSandFM")
def OSandFM():
    return render_template("OSandFM.html")


@app.route("/internet_browsing")
def internet_browsing():
    return render_template("internet_browsing.html")


@app.route("/file_management")
def file_management():
    return render_template("file_management.html")


@app.route("/typing_skills")
def typing_skills():
    return render_template("typing_skills.html")


@app.route("/msword")
def msword():
    return render_template("msword.html")


@app.route("/mspowerpoint")
def mspowerpoint():
    return render_template("mspowerpoint.html")


@app.route("/mssheets")
def mssheets():
    return render_template("mssheets.html")

@app.route("/websitecreation")
def websitecreation():
    return render_template("websitecreation.html")

@app.route("/intro_to_coding")
def intro_to_coding():
    return render_template("introtocoding.html")






# Display a course quiz
@app.route("/quiz/<course>")
def show_quiz(course):
    questions = QUIZZES.get(course)

    if questions is None:
        return "Course not found", 404

    # Never send the correct answers to the quiz page
    public_questions = [
        {
            "id": q["id"],
            "unit": q["unit"],
            "question": q["question"],
            "options": q["options"]
        }
        for q in questions
    ]

    return render_template(
        "quizzes/quiz.html",
        course=course,
        questions=public_questions
    )


# Display recommended practice
@app.route("/practice/<course>")
def show_practice(course):
    result = session.get(f"quiz_{course}")

    # Require a completed quiz first
    if result is None:
        return redirect(url_for("show_quiz", course=course))

    # Only students scoring below 40% need this practice page
    if result["percentage"] >= 40:
        return redirect(url_for("show_quiz", course=course))

    practice_data = PRACTICE.get(course, {})

    recommended = {
        unit: practice_data.get(unit, [])
        for unit in result["wrong_units"]
        if practice_data.get(unit)
    }

    return render_template(
        "practice/practice.html",
        course=course,
        practice_by_unit=recommended
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)