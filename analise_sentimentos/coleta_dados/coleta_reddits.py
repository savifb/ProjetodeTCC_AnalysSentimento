import praw
import os


# Conectando à API do Reddit
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)


#teste de autenticação
try:
    user = reddit.user.me()
    if user:
        print(f'Autenticado como: {user}')
    else:
        print('Erro na autenticação')
except praw.exceptions.APIException as api_ex:
    print(f'Erro de API: {api_ex}')
except praw.exceptions.ClientException as client_ex:
    print(f'Erro de Cliente: {client_ex}')
except praw.exceptions.PRAWException as praw_ex:
    print(f'Erro do PRAW: {praw_ex}')
except praw.exceptions.AuthenticationException as auth_ex:
    print(f'Erro de Autenticação: {auth_ex}')
except praw.exceptions.OAuthException as oauth_ex:
    print(f'Erro de OAuth: {oauth_ex}')
except Exception as e:
    print(f'Erro desconhecido: {e}')
    print(f'Erro desconhecido: {e}')