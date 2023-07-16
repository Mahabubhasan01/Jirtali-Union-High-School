from django.shortcuts import render

# Create your views here.


def Home(request):
    teachers = [
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Honufa Islam",
            "role": 'Bangla',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Shilpi Akter",
            "role": 'General Science',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Saiful Islam",
            "role": 'Math Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Ummey Honey",
            "role": 'General Science',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Nannu Khan",
            "role": 'Scial Science',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Uttam Kumar",
            "role": 'English Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Bellal Khan",
            "role": 'Accounting',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Songkar pal",
            "role": 'Bangla Grammar',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
        {"name": "Salma Sultana",
            "role": 'Head Teacher',
            "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational."
         },
    ]

    students = [
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/0YKGRWF/download.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/cbbRCtX/images-1.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/M6cqx1c/images-2.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/QpN2RFG/images-3.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/c106r85/images-4.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/zs4ZXpR/images-5.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "img": "https://i.ibb.co/mRKMjvv/images-13.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/fXXtjyM/images-6.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/7zJPhHk/images-7.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/m5wXjnf/images-8.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/zry9pW7/images-9.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/DWHwkZx/images-10.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/9gDpgF3/images-11.jpg"

         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/MhhTc8z/images-14.jpg"


         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/H7S2H8r/images-12.jpg"


         },
        {"name": "John Smith",
         "gpa": 5.00,
         "motto": "Achieve greatness through education, perseverance, and a relentless spirit.",
         "session": 2020,
         "img": "https://i.ibb.co/yk5p7Fd/images-15.jpg"


         },

    ]
    """ https://i.ibb.co/0YKGRWF/download.jpg
    https://i.ibb.co/cbbRCtX/images-1.jpg
    https://i.ibb.co/M6cqx1c/images-2.jpg
    https://i.ibb.co/QpN2RFG/images-3.jpg
    https://i.ibb.co/c106r85/images-4.jpg
    https://i.ibb.co/zs4ZXpR/images-5.jpg
    https://i.ibb.co/fXXtjyM/images-6.jpg
    https://i.ibb.co/7zJPhHk/images-7.jpg
    https://i.ibb.co/m5wXjnf/images-8.jpg
    https://i.ibb.co/zry9pW7/images-9.jpg
    https://i.ibb.co/DWHwkZx/images-10.jpg
    https://i.ibb.co/9gDpgF3/images-11.jpg
    https://i.ibb.co/H7S2H8r/images-12.jpg
    https://i.ibb.co/mRKMjvv/images-13.jpg
    https://i.ibb.co/MhhTc8z/images-14.jpg
    https://i.ibb.co/yk5p7Fd/images-15.jpg
    https://i.ibb.co/PGgkCMy/images.jpghttps://i.ibb.co/LrwqkN3/download-1.jpg """
    carousel = [
        {
            'title': 'Main office building',
            "img": "https://i.ibb.co/FJZvgr9/photo-1546410531-bb4caa6b424d.png",
            "info": ""
        },
        {
            'title': 'Academics building',
            "img": "https://i.ibb.co/YLrC92S/photo-1494949649109-ecfc3b8c35df.png",
            "info": ""
        },
        {
            'title': 'Scienece building',
            "img": "https://i.ibb.co/YLrC92S/photo-1494949649109-ecfc3b8c35df.png",
            "info": ""
        },
        {
            'title': 'Commerce building',
            "img": "https://i.ibb.co/hYk4dJv/photo-1509062522246-3755977927d7.png",
            "info": ""
        },
        {
            'title': 'Arts building',
            "img": "https://i.ibb.co/mcQXyx4/photo-1588075592446-265fd1e6e76f.png",
            "info": ""
        },
        {
            'title': 'School playgorund',
            "img": " https://i.ibb.co/4T9wLmB/photo-1591123120675-6f7f1aae0e5b.png",
            "info": ""
        },
    ]

    return render(request, 'core/home.html', {'teachers': teachers, 'students': students, "carousel": carousel})


def Dashboard(request):

    dashnav = [
        {
            "url-name": "dashboard-home",
            "icon_name": "bx bx-grid-alt",
            "nav_name": "Dashboard",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-group",
            "nav_name": "Teachers",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-group",
            "nav_name": "Students",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-edit-alt",
            "nav_name": "Attendance",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-notepad",
            "nav_name": "Results",
        },
        {
            "url-name": "",
            "icon_name": "bx bxs-edit",
            "nav_name": "Exams",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-right-indent",
            "nav_name": "Classes",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-columns",
            "nav_name": "Sections",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-money",
            "nav_name": "Fee",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-group",
            "nav_name": "Staffs",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-group",
            "nav_name": "Users",
        },
        {
            "url-name": "",
            "icon_name": "bx bxs-user-detail",
            "nav_name": "Profile",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-pie-chart-alt-2",
            "nav_name": "Analytics",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-bell",
            "nav_name": "Notifications",
        },
        {
            "url-name": "",
            "icon_name": "bx bx-cog",
            "nav_name": "Settings",
        },
    ]

    return render(request, 'core/dashboard/dashboardNav.html', {"navs": dashnav})


def Dashbord_Home(request):
    return render(request, 'core/dashboard/dashboardhome.html')
