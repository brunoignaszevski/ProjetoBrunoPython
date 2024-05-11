import gspread

credentials = {
    "installed": {
        "client_id": "12345678901234567890abcdefghijklmn.apps.googleusercontent.com",
        "project_id": "my-project1234",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        ...
    }
}
authorized_user = {
    "refresh_token": "8//ThisALONGTOkEn....",
    "token_uri": "https://oauth2.googleapis.com/token",
    "client_id": "12345678901234567890abcdefghijklmn.apps.googleusercontent.com",
    "client_secret": "MySecRet....",
    "scopes": [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
    "expiry": "1070-01-01T00:00:00.000001Z"
}
gc, authorized_user = gspread.oauth_from_dict(credentials, authorized_user)

sh = gc.open("Example spreadsheet")

print(sh.sheet1.get('A1'))