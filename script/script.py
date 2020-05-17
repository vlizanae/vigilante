import json
import logging
from speedtest import Speedtest

logging.basicConfig(level=logging.INFO, filename='data.log', format='%(message)s')

st = Speedtest()
st.get_best_server()
st.download()
st.upload()
logging.info(json.dumps(st.results.dict()))
