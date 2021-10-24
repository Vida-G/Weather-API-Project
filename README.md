# Weather API
This project provides the required APIs for creating, updating, receiving, and deleting different weather conditions.

## API details
### Create a new weather condition
Request type: `POST`

Request URL: https://weather-api-vg.herokuapp.com/api/weathers

Example input: 
```json
{
    "name": "Tornado",
    "description": "clouds, strong wind, rain, hail",
    "city": "Boston",
    "country": "USA",
    "temperature": "61 F",
    "wind_speed": "19 mph",
    "date_created": "March 12, 2015"
}
```
Example output:
```json
{
    "city": "Boston",
    "country": "USA",
    "date_created": "2015-03-12T00:00:00",
    "description": "clouds, strong wind, rain, hail",
    "id": "6bGgofoqcRLR0BneaP4BTzgfRel4W2QmkrSNKcYzazw",
    "name": "Tornado",
    "temperature": "61 F",
    "wind_speed": "19 mph"
}
```
### Update an existing weather condition
Request type: `POST`

Request URL: [https://weather-api-vg.herokuapp.com/api/weathers/\<id>](https://weather-api-vg.herokuapp.com/api/weathers/\<id>)

Example input: 
```json
{
    "name": "Tornado",
    "description": "clouds, strong wind, rain, hail",
    "city": "Chicago",
    "country": "USA",
    "temperature": "62 F",
    "wind_speed": "19 mph",
    "date_created": "March 12, 2015"
}
```
Example output:
```json
{
    "city": "Chicago",
    "country": "USA",
    "date_created": "2015-03-12T00:00:00",
    "description": "clouds, strong wind, rain, hail",
    "id": "v6Q-7uOwNI9JLFfAJsOplZUsGyRvHwgLb5cs5itZrAY",
    "name": "Tornado",
    "temperature": "62 F",
    "wind_speed": "19 mph"
}
```

### Get all weather conditions
Request type: `GET`

Request URL: https://weather-api-vg.herokuapp.com/api/weathers

Example output:
```json
[
  {
    "city": "Chicago",
    "country": "USA",
    "date_created": "2015-03-12T00:00:00",
    "description": "clouds, strong wind, rain, hail",
    "id": "v6Q-7uOwNI9JLFfAJsOplZUsGyRvHwgLb5cs5itZrAY",
    "name": "Tornado",
    "temperature": "62 F",
    "wind_speed": "19 mph"
  },
  {
    "city": "Boston",
    "country": "USA",
    "date_created": "2015-03-12T00:00:00",
    "description": "clouds, strong wind, rain, hail",
    "id": "6bGgofoqcRLR0BneaP4BTzgfRel4W2QmkrSNKcYzazw",
    "name": "Tornado",
    "temperature": "61 F",
    "wind_speed": "19 mph"
  }
]
```
### Get a weather condition
Request type: `GET`

Request URL: [https://weather-api-vg.herokuapp.com/api/weathers/\<id>](https://weather-api-vg.herokuapp.com/api/weathers/\<id>)

Example output: 
```json
{
    "city": "Chicago",
    "country": "USA",
    "date_created": "2015-03-12T00:00:00",
    "description": "clouds, strong wind, rain, hail",
    "id": "v6Q-7uOwNI9JLFfAJsOplZUsGyRvHwgLb5cs5itZrAY",
    "name": "Tornado",
    "temperature": "62 F",
    "wind_speed": "19 mph"
}
```

### Delete a weather condition
Request type: `DELETE`

Request URL: [https://weather-api-vg.herokuapp.com/api/weathers/\<id>](https://weather-api-vg.herokuapp.com/api/weathers/\<id>)

Example output:
```json
{
    "Success": "ID #6bGgofoqcRLR0BneaP4BTzgfRel4W2QmkrSNKcYzazw has been deleted"
} 
```