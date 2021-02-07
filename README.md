# automate-AWS-SSO
Automate automate AWS SSO access keys retrieval.

## Login
Login first time manually 
```
python sso_auth.py
```

## Save creds into file
Save DEV and QA creds
```
python sso_get_creds.py
```

    "DEV" keys are saved to ".creds\DEV.txt"
    "QA" keys are save to ".creds\QA.txt"