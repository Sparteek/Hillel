XPATH_LOCATORS = {
    # Головна сторінка
    "header": "//header",
    "header_logo": "//header//a[contains(@class, 'header_logo')]",
    "home_link": "//header//a[text()='Home']",
    "about_button": "//header//button[text()='About']",
    "contacts_button": "//header//button[text()='Contacts']",
    "guest_login_button": "//header//button[text()='Guest log in']",
    "sign_in_button": "//header//button[text()='Sign In']",
    "header_navigation": "//header//nav[contains(@class, 'header_nav')]",
    "header_navigation_buttons": "//header//nav[contains(@class, 'header_nav')]//button",
    "header_right_block": "//header//div[contains(@class, 'header_right')]",

    # Footer
    "footer": "//footer",
    "footer_school_text": "//footer//p[text()='© 2021 Hillel IT school']",
    "footer_description": "//footer//p[contains(text(), 'educational purposes')]",
    "footer_logo": "//footer//a[@href='/']",

    # Вікно входу
    "sign_in_modal": "//app-signin-modal",
    "login_title": "//app-signin-modal//h4[text()='Log in']",
    "close_modal_button": "//app-signin-modal//button[@aria-label='Close']",
    "login_form": "//app-signin-modal//form",
    "email_label": "//app-signin-form//label[text()='Email']",
    "email_input": "//app-signin-form//input[@id='signinEmail']",
    "password_label": "//app-signin-form//label[text()='Password']",
    "password_input": "//app-signin-form//input[@id='signinPassword']",
    "remember_checkbox": "//app-signin-form//input[@id='remember']",
    "registration_button": "//app-signin-modal//button[text()='Registration']",
    "login_button": (
        "//app-signin-modal"
        "//div[contains(@class, 'modal-footer')]"
        "//button[contains(@class, 'btn-primary')]"
    ),
}


CSS_LOCATORS = {
    # Головна сторінка
    "header": "header.header",
    "header_inner": "header .header_inner",
    "header_left_block": "header .header_left",
    "header_logo": "header a.header_logo",
    "header_logo_svg": "header a.header_logo > svg",
    "header_navigation": "header nav.header_nav",
    "home_link": "header nav.header_nav > a.header-link",
    "navigation_buttons": "header nav.header_nav > button.header-link",
    "header_right_block": "header .header_right",
    "sign_in_button": "header button.header_signin",

    # Footer
    "footer": "footer.footer",
    "footer_container": "footer.footer > .container",
    "footer_left_block": "footer .footer_item.-left",
    "footer_first_paragraph": "footer .footer_item.-left > p:first-child",
    "footer_second_paragraph": "footer .footer_item.-left > p:nth-child(2)",
    "footer_logo": "footer a.footer_logo[href='/']",

    # Вікно входу
    "sign_in_modal": "app-signin-modal",
    "modal_header": "app-signin-modal .modal-header",
    "modal_title": "app-signin-modal h4.modal-title",
    "close_modal_button": "app-signin-modal button[aria-label='Close']",
    "login_form": "app-signin-modal .modal-body form",
    "email_input": "app-signin-form input#signinEmail[name='email']",
    "password_input": "app-signin-form input#signinPassword[type='password']",
    "remember_checkbox": "app-signin-form input#remember[type='checkbox']",
    "login_button": "app-signin-modal .modal-footer > button.btn-primary",
}
