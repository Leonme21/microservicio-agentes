from dotenv import load_dotenv; import os; from supabase import create_client
load_dotenv()
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
try:
    client = create_client(url, key)
    res = client.table('agentes').select('*').execute()
    print('SUCCESS:', res.data)
except Exception as e:
    import traceback
    traceback.print_exc()
