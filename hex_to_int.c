/*
 * Author: Fahad Zaheer
 * Date: 18th November, 2022
 */
#include<stdio.h>
#include<stdlib.h>

int main(){
    char str[7] = "0x1f\0"; // 0x1f = 31
    char new_str[8]; // a new string to store integer value
    long num = strtol(str, NULL, 16); // convert hex string to a long
    int i = 0; // counter

    sprintf(new_str, "%ld", num); // convert long to string

    puts(str); // print hex string

    // print integer string and check for null terminator
    while (new_str[i] != '\0'){
        printf("%c", new_str[i]);
        i++;
    }
    // print new line
    printf("\n");

    return 0;
}