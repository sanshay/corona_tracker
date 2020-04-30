from flask import Flask, render_template
import requests
app = Flask(__name__)
statewise_list = requests.get("https://api.covid19india.org/data.json").json()['statewise']


def clean_raw_list():
    clean_list = []
    for item in statewise_list:
        item.pop('deltaconfirmed')
        item.pop('deltadeaths')
        item.pop('deltarecovered')
        item.pop('lastupdatedtime')
        item.pop('statecode')
        item.pop('statenotes')
        clean_list.append(list(item.values()))

    return clean_list
    

def get_total():
    total_list = clean_list[0]
    clean_list.pop(0) # remove the first entry as its 'total'
    return total_list

clean_list = clean_raw_list()
total_list = get_total()

def make_jinja_dict():
    # every list has 4 index [a,b,c,d,e]
    # a -> active
    # b -> confirmed
    # c -> deaths
    # d -> recovered
    # e -> state ( == 'total' if total_list else a statename )
    
    return {'total_list': total_list, 'clean_list': clean_list}



@app.route('/')
def home():
	return render_template('home.html', clean_list=clean_list, total_list=total_list)







if __name__ == "__main__":
	app.run(debug=True)