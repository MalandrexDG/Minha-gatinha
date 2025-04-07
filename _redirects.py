# Criar o arquivo _redirects com o conteúdo correto
redirects_content = "/*    /index.html   200\n"

file_path = "/mnt/data/_redirects"
with open(file_path, "w") as file:
    file.write(redirects_content)

file_path
