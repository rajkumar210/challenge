mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless=true\n\
port=$PORT\n\
enableCORS=fales\n\
\n\
" > ~/.streamlit/config.toml
