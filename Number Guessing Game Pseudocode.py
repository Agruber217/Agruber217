BEGIN  
    SET lower_bound = 1  
    SET upper_bound = 100  
    GENERATE random_number between lower_bound and upper_bound  
    SET guess = 0  
    
    WHILE guess is not equal to random_number DO  
        DISPLAY "Enter your guess: "  
        READ guess  
        
        IF guess < random_number THEN  
            DISPLAY "Too low! Try again."  
        ELSE IF guess > random_number THEN  
            DISPLAY "Too high! Try again."  
        ELSE  
            DISPLAY "Congratulations! You guessed the correct number."  
        ENDIF  
    ENDWHILE  
END  
