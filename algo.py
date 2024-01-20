from OddsJamClient import OddsJamClient;
from dotenv import load_dotenv
import os
load_dotenv()
ODDSJAM_API_KEY = os.getenv("ODDSJAM_API_KEY")
Client = OddsJamClient(ODDSJAM_API_KEY);

Client.UseV2();
v2Results = Client.GetLeagues(); #v2 endpoints
# print(v2Results.keys)
for key, value in v2Results:
    print (key, value)