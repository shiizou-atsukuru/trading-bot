import streamlit as st
import pandas as pd
import os
from bot.orders import place_limit_order, place_market_order
from bot.logger import LOG_FILE

st.set_page_config(page_title="Binance OMS", layout="wide")

if 'staged_orders' not in st.session_state:
    st.session_state.staged_orders = []

st.title("Order Management System")

with st.expander("+ Add Manual Order", expanded=True):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: sym = st.text_input("Symbol", "BTCUSDT")
    with col2: side = st.selectbox("Side", ["BUY", "SELL"])
    with col3: o_type = st.selectbox("Type", ["MARKET", "LIMIT"])
    with col4: qty = st.number_input("Qty", value=0.002, step=0.001, format="%.4f")
    with col5: price = st.number_input("Price", value=0.0) if o_type == 'LIMIT' else None

    if st.button("Add to Stage"):
        new_order = {"symbol": sym, "side": side, "type": o_type, "quantity": qty, "price": price}
        st.session_state.staged_orders.append(new_order)
        st.toast(f"Added {sym} to staging!")

with st.expander("Import Orders"):
    uploaded_file = st.file_uploader("Upload CSV (Symbol,Side,Type,Qty,Price)", type="csv")
    if uploaded_file:
        try:
            df_imported = pd.read_csv(uploaded_file)
            st.write('### Preview of Uploaded File')
            st.dataframe(df_imported.head(), width="stretch")

            if st.button("Confirm and Add to Stage"):
                new_orders = df_imported.to_dict('records')

                st.session_state.staged_orders.extend(new_orders)

                st.success(f"Successfully imported {len(new_orders)} orders!")
                st.rerun()
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

st.header("Staged Orders")
if st.session_state.staged_orders:
    df = pd.DataFrame(st.session_state.staged_orders)
    st.table(df)

    col_ex, col_cl = st.columns([1,8])
    if col_ex.button("EXECUTE", type="primary"):
        results_box = st.container(border=True)
        results_box.write("### Execution Status")

        for idx, order in enumerate(st.session_state.staged_orders):
            with st.spinner(f"Executing {order['symbol']}..."):
                if order['type'] == 'MARKET':
                    res = place_market_order(order['symbol'], order['side'], order['quantity'])
                else:
                    res = place_limit_order(order['symbol'], order['side'], order['quantity'], order['price'])
                
                if "error" in res:
                    results_box.error(f"Row {idx+1}: {order['symbol']} - {res['error']}")
                else:
                    results_box.success(f"Row {idx+1}: {order['symbol']} - SUCCESS (ID: {res['orderId']})")

        st.session_state.staged_orders = []
        st.balloons()

    if col_cl.button("Clear Stage"):
        st.session_state.staged_orders = []
        st.rerun()

else:
    st.info("No orders in staging. Add manually or upload a file.")


with st.sidebar:
    st.header("System Controls")     
    st.divider()

    st.header("System Logs")
    if st.button("Refresh Logs"):
        st.rerun()

    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                log_content = "".join(f.readlines()[-20:])
                st.text_area("Live Feed", value=log_content, height=300)
        else:
            st.info("Log file initialized but empty.")
    except FileNotFoundError:
        st.write("No logs yet.")
    except Exception as e:
        st.write(f"Error reading logs: {e}")

    if st.button("Clear Log File", type="secondary", use_container_width=True):
        try:
            with open(LOG_FILE, "w") as f:
                f.write("")
            st.toast("Logs cleared!")
            st.rerun()
        except Exception as e:
            st.error(f"Could not clear logs: {e}")