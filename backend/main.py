"""Backend linking to SuperTokens core."""
from fastapi import FastAPI
from secrect_strs import GOOGLE_0AUTH_CLIENT_SECRET, SUPERTOKENS_API
from starlette.middleware.cors import CORSMiddleware
from supertokens_python import (
    get_all_cors_headers,
    init,
    InputAppInfo,
    SupertokensConfig,
)
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe import session, thirdpartyemailpassword
from supertokens_python.recipe.thirdpartyemailpassword import Google


init(
    app_info=InputAppInfo(
        app_name='stlogin',
        api_domain='https://stokensdemo-1-z8458742.deta.app/',
        website_domain='http://localhost',
        api_base_path='/auth',
        website_base_path='/auth',
    ),
    supertokens_config=SupertokensConfig(
        # https://try.supertokens.com is for demo purposes. core url
        connection_uri='https://dev-b580f341bf9611edbd48135fc52bc1b6'
        + '-ap-southeast-1.aws.supertokens.io:3572',
        api_key=SUPERTOKENS_API,
    ),
    framework='fastapi',
    recipe_list=[
        session.init(),  # initializes session features
        thirdpartyemailpassword.init(
            # Inside init
            providers=[
                # We have provided you with development keys which you can use for testing.
                # IMPORTANT: Please replace them with your own OAuth keys for production use.
                Google(
                    client_id='327020114390-ggc01io6rm7o7h5k772kgon9nd3mch8k'
                    + '.apps.googleusercontent.com',
                    client_secret=GOOGLE_0AUTH_CLIENT_SECRET
                    # ), Facebook(
                    #     client_id='FACEBOOK_CLIENT_ID',
                    #     client_secret='FACEBOOK_CLIENT_SECRET'
                ),
            ]
        ),
    ],
    mode='asgi',  # use wsgi if you are running using gunicorn
)


app = FastAPI()
app.add_middleware(get_middleware())

# TODO: Add APIs

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost'],
    allow_credentials=True,
    allow_methods=['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'PATCH'],
    allow_headers=['Content-Type'] + get_all_cors_headers(),
)

# TODO: start server
