import datetime
import functions_framework
from enrich import process_date_range


@functions_framework.cloud_event
def enrich_billing_data(cloud_event):
    print("Enrich billing data CF called: Starting function..")

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=3)

    process_date_range(start_date, end_date)

    print("Enrich billing data CF finished..")
    return 
