import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

stdio_transport = StdioTransport(
    command="npx",
    args=["-y", "@upstash/context7-mcp"]
)

stdio_client = Client(stdio_transport)

async def main():
    async with stdio_client as client:
        #list of tools the server provides
        tools=await client.list_tools()
        print("="*60)
        print("number of tools:",len(tools))
        print("="*60)
        print("names of tools 1:",tools[0].name)
        print("="*60)
        print("description of tools 1:",tools[0].description[:100])
        print("="*60)
        print("the input schema to tools 1:",tools[0].inputSchema)
        print("="*60)
        

# call tool  # to find library id
async def main1():
    #find the library id via a search query
    async with stdio_client as client:   # name of tools 1 is: resolve-library-id which is called below
        response=await client.call_tool("resolve-library-id",{
            "libraryName":"fastmcp",
            "query":"i want to create a new MCP server using the fastmcp python framework"
        })
        print(response.content[0].text)
        
        
# Query docs
# now we'll use the query-docs tool to retrieve the actual documentation
# for that specific library

async def query_docs():
    async with stdio_client as client:
        docs=await client.call_tool("query-docs",{
            "libraryId":"/llmstxt/gofastmcp_llms-full_txt",
            "query":"i want to fetch the code snippets and the documentation",
            "tokens":5000
        })
        print(docs.content[0].text[:1000])
        
        
# Question 1. How do you use the resolve-library-id tool to find the library ID for scikit-learn

async def scikit_learn_library():
    #find the library id via a search query
    async with stdio_client as client:
        response=await client.call_tool("resolve-library-id",{
            "libraryName":"scikit-learn",
            "query":"i want to use skikit-learn"
        })
        print(response.content[0].text)

# Question 2. How do you get the actual documentation once you have the library ID?        

async def scikit_learn_library_query_docs():
    async with stdio_client as client:
        docs=await client.call_tool("query-docs",{
            "libraryId":"/websites/scikit-learn_dev",
            "query":"i want to fetch the code snippet about linear regression",
            "tokens":1000
        })
        print(docs.content[0].text)


if __name__=="__main__":
    asyncio.run(scikit_learn_library_query_docs())