"""Backend linking to SuperTokens core."""

from fastapi import FastAPI
from secrect_strs import SUPERTOKENS_API
from starlette.middleware.cors import CORSMiddleware
from supertokens_python import (
    get_all_cors_headers,
    init,
    InputAppInfo,
    SupertokensConfig,
)
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe import passwordless, session

from supertokens_python.recipe.passwordless import ContactEmailOnlyConfig

init(
    app_info=InputAppInfo(
        app_name='stlogin',
        api_domain='http://localhost:8000',
        website_domain='http://localhost',
        api_base_path='/auth',
        website_base_path='/auth',
    ),
    supertokens_config=SupertokensConfig(
        # These are the connection details of the app you created on supertokens.com
        connection_uri='https://dev-b580f341bf9611edbd48135fc52bc1b6'
        + '-ap-southeast-1.aws.supertokens.io:3572',
        api_key=SUPERTOKENS_API,
    ),
    framework='fastapi',
    recipe_list=[
        session.init(),  # initializes session features
        passwordless.init(
            flow_type='USER_INPUT_CODE_AND_MAGIC_LINK',
            contact_config=ContactEmailOnlyConfig(),
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
