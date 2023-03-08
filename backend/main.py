from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import session, thirdpartyemailpassword

init(
    app_info=InputAppInfo(
        app_name='stlogin',
        api_domain='https://xxxxx.deta.space',
        website_domain='http://localhost',
        api_base_path='/auth',
        website_base_path='/auth',
    ),
    supertokens_config=SupertokensConfig(
        # https://try.supertokens.com is for demo purposes. Replace this with the address of your core instance (sign up on supertokens.com), or self host a core.
        connection_uri='https://try.supertokens.com',
        # api_key=<API_KEY(if configured)>
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
