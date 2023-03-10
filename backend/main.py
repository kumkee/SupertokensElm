from secrect_strs import SUPERTOKENS_API
from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import session, thirdpartyemailpassword

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
            # TODO: See next step
        ),
    ],
    mode='asgi',  # use wsgi if you are running using gunicorn
)
