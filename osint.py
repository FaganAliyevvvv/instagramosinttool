import instaloader

def instagram_osint(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        data = {
            "Username": profile.username,
            "Tam Adı": profile.full_name,
            "Bio": profile.biography,
            "Takipçi Sayı": profile.followers,
            "Takip Etdikləri": profile.followees,
            "Profil Fotoları Linki": profile.profile_pic_url,
            "Hesab Növü": "Public" if profile.is_private is False else "Private",
            "Postların Sayı": profile.mediacount
        }

        for key, value in data.items():
            print(f"{key}: {value}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Hədəf istifadəçi adı '{username}' tapılmadı!")
    except Exception as e:
        print(f"Xəta baş verdi: {e}")

print('''
########    ###     ######      ###    ##    ## 
##         ## ##   ##    ##    ## ##   ###   ## 
##        ##   ##  ##         ##   ##  ####  ## 
######   ##     ## ##   #### ##     ## ## ## ## 
##       ######### ##    ##  ######### ##  #### 
##       ##     ## ##    ##  ##     ## ##   ### 
##       ##     ##  ######   ##     ## ##    ## 
''')
target_username = input("Hədəf username: ")
instagram_osint(target_username)
