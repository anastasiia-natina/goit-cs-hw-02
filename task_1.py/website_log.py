#!/bin/bash

websites=(
    "https://google.com"
    "https://facebook.com"
    "https://twitter.com"
)
log_file = "website_status.log"

#> "$log_file"

check_website() {
    
    if curl -sL -head "$1" | grep "200" > /dev/null; then
        echo "$1 is up"
        echo "$1 is up" >> "$log_file"
        
    else
        echo "$1 is down"
        echo "$1 is down" >> "$log_file"
        
    fi
}
    

for website in "$websites[@]"; do
    check_website ("$websites")
done

echo ("Results have logged to: $log_file")