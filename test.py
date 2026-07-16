from agents.customer_graph.graph import graph

state = {

    "messages":[

        {

            "role":"user",

            "message":"My Outlook won't open."

        }

    ],

    "title":"",

    "description":"",

    "ticket_ready":False,

    "resolution_status":"",

    "category":"",

    "level":1,

    "response":""

}

print(graph.invoke(state))