from Adm import Admin,Privileges
privileges = ["can add post", "can delete post", "can ban user",]
administrator = Admin("William","Cesar",20,"Male",privileges)
administrator.privileges.show_privileges()
