# Eurobot2020 Camera Unit
Image processing unit with web server publishing predicted data

# Image processing unit
* Open CV script
* Machine learning model


# Web server
Http server with REST API endpoints:


http://192.168.0.1/becaon_1/side
```
data:{
  "side" : "north"
}
```

http://192.168.0.1/becaon_2/side
```
data:{
  "side" : "south"
}
```

# Script checking beacon readings and calculate prediction 
http://192.168.0.1/preducted_side

```
data:{
  "pred_side" : "north"
}
```
