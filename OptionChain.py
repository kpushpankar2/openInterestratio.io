import json
import requests
import streamlit as st


@st.cache_data
def getCurrentPCR(symbol):
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=' + symbol
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'
    }

    response = requests.get(url, headers=headers).content
    data = json.loads(response.decode('utf-8'))['filtered']['data']

    change_in_CE = 0
    change_in_PE = 0
    for idx in range(len(data)):
        change_in_CE += data[idx]['CE']['changeinOpenInterest']
        change_in_PE += data[idx]['PE']['changeinOpenInterest']

    return (change_in_PE / change_in_CE)


def main():
    st.title("PCR Values")

    pcr = getCurrentPCR('BANKNIFTY')
    pcr1 = getCurrentPCR('NIFTY')

    st.write(f"PCR of BANKNIFTY: {pcr}")
    st.write(f"PCR of NIFTY: {pcr1}")


if __name__ == "__main__":
    main()
