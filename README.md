## セットアップのしかた

```sh
git clone これ
cd それ
virtualenv .
pip install -r requirements.txt
pip list
```

## 最初に作ったときやったこと

```sh
# https://github.com/googleapis/google-api-python-client#maclinux
pip3 install virtualenv
virtualenv gcp-client
cd gcp-client
source bin/activate
bin/pip install google-api-python-client
```

## 実行

`python get-users-list.py`

# 参考

- https://stackoverflow.com/questions/60550929/google-admin-sdk-with-service-account-without-impersonation/60578000#60578000
- https://stackoverflow.com/questions/62200462/directory-v1-always-returns-403-from-a-cloud-function
- https://qiita.com/hiren/items/c9a199a3a8949c5b30d1

### ちょっと違うけど参考

- https://qiita.com/Hikosaburou/items/44557cc3892174797b78

### google-api-python-client API Docs

https://googleapis.github.io/google-api-python-client/docs/dyn/admin_directory_v1.users.html

### Python じゃなくて Nodejs でどうやるか

GoogleAuth オブジェクトじゃなくて JWT を使って subject を指定する。

- https://github.com/googleapis/google-api-nodejs-client/issues/1699#issuecomment-812411745

## gcloud --help

```
--impersonate-service-account=SERVICE_ACCOUNT_EMAILS

For this gcloud invocation, all API requests will be made as the given service account or target service account in an impersonation delegation chain instead of the currently selected account. You can specify either a single service account as the impersonator, or a comma-separated list of service accounts to create an impersonation delegation chain. The impersonation is done without needing to create, download, and activate a key for the service account or accounts.
In order to make API requests as a service account, your currently selected account must have an IAM role that includes the iam.serviceAccounts.getAccessToken permission for the service account or accounts.
The roles/iam.serviceAccountTokenCreator role has the iam.serviceAccounts.getAccessToken permission. You can also create a custom role.
You can specify a list of service accounts, separated with commas. This creates an impersonation delegation chain in which each service account delegates its permissions to the next service account in the chain. Each service account in the list must have the roles/iam.serviceAccountTokenCreator role on the next service account in the list. For example, when --impersonate-service-account= SERVICE_ACCOUNT_1,SERVICE_ACCOUNT_2, the active account must have the roles/iam.serviceAccountTokenCreator role on SERVICE_ACCOUNT_1, which must have the roles/iam.serviceAccountTokenCreator role on SERVICE_ACCOUNT_2. SERVICE_ACCOUNT_1 is the impersonated service account and SERVICE_ACCOUNT_2 is the delegate.
Overrides the default auth/impersonate_service_account property value for this command invocation.
```

```
--impersonate-service-account=SERVICE_ACCOUNT_EMAILS

このgcloud呼び出しでは、すべてのAPIリクエストは、現在選択されているアカウントではなく、与えられたサービスアカウントまたはなりすまし委任チェーンのターゲットサービスアカウントとして行われます。なりすましとして単一のサービスアカウントを指定するか、なりすまし委任チェーンを作成するためにサービスアカウントのカンマ区切りのリストを指定することができます。なりすましは、サービスアカウントの鍵の作成、ダウンロード、有効化を必要としません。
サービスアカウントとしてAPIリクエストを行うには、現在選択されているアカウントが、サービスアカウントまたはアカウントのiam.serviceAccounts.getAccessTokenパーミッションを含むIAMロールを持つ必要があります。
roles/iam.serviceAccountTokenCreatorロールは、iam.serviceAccounts.getAccessTokenパーミッションを有しています。また、カスタムロールを作成することもできます。
サービスアカウントのリストをカンマで区切って指定することができます。これにより、各サービスアカウントが次のサービスアカウントに権限を委譲する、なりすまし委譲チェーンが作成されます。リスト内の各サービスアカウントは、リスト内の次のサービスアカウントに roles/iam.serviceAccountTokenCreator ロールを持つ必要があります。例えば、--impersonate-service-account= SERVICE_ACCOUNT_1,SERVICE_ACCOUNT_2 の場合、アクティブなアカウントはSERVICE_ACCOUNT_1に roles/iam.serviceAccountTokenCreator ロールを持たなければならず、それはSERVICE_ACCOUNT_2に role/iam.serviceAccountTokenCreator ロールを持たねばならない。SERVICE_ACCOUNT_1は、なりすましサービスアカウントであり、SERVICE_ACCOUNT_2は、デリゲートである。
このコマンド呼び出しのデフォルトのauth/impersonate_service_accountプロパティ値をオーバーライドします。


www.DeepL.com/Translator（無料版）で翻訳しました。
```
