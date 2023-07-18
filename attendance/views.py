from django.shortcuts import render


dashnav = [
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-grid-alt",
        "nav_name": "Dashboard",
    },
    {
        "url_name": "teachers",
        "icon_name": "bx bx-group",
        "nav_name": "Teachers",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-group",
        "nav_name": "Students",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-right-indent",
        "nav_name": "Classes",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-columns",
        "nav_name": "Sections",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-book-open",
        "nav_name": "Subjects",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-edit-alt",
        "nav_name": "Attendance",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bxs-edit",
        "nav_name": "Exams",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-notepad",
        "nav_name": "Results",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-money",
        "nav_name": "Fee",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-group",
        "nav_name": "Staffs",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-group",
        "nav_name": "Users",
    },
    {
        "url_name": "",
        "icon_name": "bx bxs-user-detail",
        "nav_name": "Profile",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-pie-chart-alt-2",
        "nav_name": "Analytics",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-bell",
        "nav_name": "Notifications",
    },
    {
        "url_name": "dashboard-home",
        "icon_name": "bx bx-cog",
        "nav_name": "Settings",
    },
]
teachers = [

    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"

     },
    {"name": "Honufa Islam",
     "role": 'Bangla',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Shilpi Akter",
     "role": 'General Science',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Saiful Islam",
     "role": 'Math Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Ummey Honey",
     "role": 'General Science',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Nannu Khan",
     "role": 'Scial Science',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Uttam Kumar",
     "role": 'English Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Bellal Khan",
     "role": 'Accounting',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Songkar pal",
     "role": 'Bangla Grammar',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
    {"name": "Salma Sultana",
     "role": 'Head Teacher',
     "moto": "Innovative, charismatic, influential, visionary, approachable, inspiring, dynamic, motivational, knowledgeable, transformational.",
     "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxivAs4UknzmDfLBXGMxQkayiZDhR2ftB4jcIV7LEnIEStiUyMygioZnbLXCAND-I_xWQpVp0jv-dv9NVNbuKn4sNpXYtLIJk2-IOdWQNpC2Ldapnljifu0pnQqAWU848Ja4lT9ugQex-nwECEh3a96GXwiRXlnGEE6FFF_tKm66IGe3fzmLaVIoNL/s1600/img_avatar.png"
     },
]


def Attendance_list(request):
    return render(request, 'attendance_list.html', {'navs': dashnav, "teachers": teachers})
