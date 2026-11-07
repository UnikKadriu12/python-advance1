import strealit as st
import pandas as pd
import plotly express as px





books_df=pd.read_csv("Bestsellers_with_categories_20222_03_27.csv")


st.title("Bestselling books Analysis")
st.write("this app analyzes the Amazon Top Selling books from 2009 to 2022")


st.subheader("Summary Statistic")
tottal_books = books_df.shape[0]
unique_titles = books_df['Name'].unique()
average_rating = books_df['User rating'].mean()
average_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Books",total_books)
col2.metric("Unique Books",unique_books)
col3.metric("AVG",f"{average_rating:.2f}")
col4.metric("AVG price",f"{average_price:.2f }")


st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns(2)




with col1:
    st.header("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

with col1:
    st.header("Top 10 titles")
    top_titles = books_df['titles'].value_counts().head(10)
    st.bar_chart(top_titles)


st.subheader("Genre Distribution")
fig = px.pie(books_df,namess="Genre",title="most liked gerne(2009-2022)",color="Genre"),
             color_discrete_sequence=px.color.sequental.Plasma)
st.plotly_chart(fig)

st.subheader("Number of fictionn vs non fiction books over the years")
size = books_df.groupby(['Year','Gerne']).size().reset_index(name="Counts")
fig2 = px.bar(size, x="Year",y="Genre",
               color_discrete_sequence=px.colors.sequential.Plasma,barmode="group")
st.plotly_chart(fig2)

st.subheader("top 15 authors counts of books published")
top_authors = books_df=["Author"].value_counts().head(12).reset_index()
top_authors.column = ["Authors","Count"]

fig3 = px.bar(top_authors,x="count",y="Author",orientation="h",) 


st.plotly_chart(fig3)










