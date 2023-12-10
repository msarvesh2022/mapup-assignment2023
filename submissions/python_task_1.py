import pandas as pd

# Solution 1
df= pd.read_csv('dataset-1.csv')

def generate_car_matrix(df):
    df= df[['id_1','id_2','car']]
    df= df.pivot(index='id_1',columns='id_2',values='car').fillna(0)
    return df

print(generate_car_matrix(df))

#  Solution 2

def get_type_count(df):
    # df1= df.copy()
    df['car_type'] = df['car'].astype(int) 
    df['car_type'] = df['car_type'].apply(lambda x: 'Low' if x <= 15 else ('Medium' if  15 < x <= 25 else 'High'))
    return df

print(get_type_count(df))

# Solution 3


def get_bus_indexes(df):
    bus_mean = df['bus'].mean()
    
    # value = (bus_mean)*2

    bus_indexes = df[df['bus'] > 2 * bus_mean].index
    sorted_indexes = sorted(bus_indexes)

    return sorted_indexes

print(get_bus_indexes(df))

# Solution 4

def filter_routes(df):
    route_avg_truck = df.groupby('route')['truck'].mean()

    
    selected_routes = route_avg_truck[route_avg_truck > 7]
    sorted_routes = sorted(selected_routes)

    return selected_routes

print(filter_routes(df))



# Solution 5


def input_matrix(df):
    df=df.pivot(index='id_1',columns='id_2', values='car').fillna(0) 
    # df = df.apply(map(lambda x: x*0.75 if x >20 else x*1.25))
    df = df.applymap(lambda x: x*0.75 if x >20 else x*1.25)
    return df


print(input_matrix(df))
