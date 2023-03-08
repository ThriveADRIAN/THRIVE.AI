'''
"How Am I THAT?"
https://www.heroic.us/optimize/plus-one/how-am-i-that
'''
IF ( TRIGGERED ) {
    HOW_AM_I_THAT();
}

'''
GOAL: Practice managing reaction (Fear/Anxiety, Anger/Frustration, Digust)
and future projection.
- Avoid heart medication. This is within control. #selfcare
- "Most difficult person you are dealing with is you"

The Fastest Way to Optimize
https://www.optimize.me/plus-one/the-fastest-way-to-optimize
- What is the #1 thing you can start doing?
- What is the #1 thing you can stop doing?

Just Execute Your Game Plan
https://www.optimize.me/plus-one/just-execute-your-game-plan
'''
IF ( REACTION_TO_STIMULUS != COMFORTABLE) {
    BREATHE_AND_STOP();
    LISTEN();
    UNDERSTAND();
    RESPOND();
}
'''
+1's
- How to listen like a therapist: 4 secret skills https://www.youtube.com/watch?v=UVN96JhDOmg
- Think Win/Win +https://www.optimize.me/plus-one/think-win-win
- "Frankl on Freedom" https://www.optimize.me/plus-one/frankl-on-freedom
'''

IF ( ANXIETY > 0) {
    '''
    No breath, no life!
    Optimal Breathing 101 https://www.optimize.me/101/optimal-breathing
    '''
    BREATHE_LESS();
    BREATHE_RIGHT();

    '''
    PM RITUAL BOOKEND
    Best Day Starts the Night Before.
    PM Counts Twice https://www.optimize.me/plus-one/pm-counts-twice
    '''
    PRIORITIZE_SLEEP();
    SHUTDOWN_COMPLETE();
    DIGITAL_SUNSET();
    
    '''
    AM RITUAL BOOKEND
    Start the day with focusing on what is within our control.
    Be creative before reactive. #MakeYourself #MasterpieceDays
    AM + PM Bookends https://www.optimize.me/plus-one/am-pm-bookends
    '''
    WAKE_WITH_PURPOSE();
    HYDRATE();
    AM_MEDITATION();
    AM_MOVEMENT();
    HEALTHY_BREAKFAST();
    OSCILLATE(); '''Start Gymboss Plus Timer 1% (14:24)'''
    
    '''
    INPUT MODULATION
    None are as important as you
    '''
    REDUCE_INPUTS();
}
'''
+1's
- Ikigai https://www.optimize.me/plus-one/ikigai
- A 2:43 Heroic Meditation https://www.optimize.me/plus-one/a-243-heroic-meditation'
- Movement > Exercise https://www.optimize.me/plus-one/movement-exercise
- Eat Food https://www.optimize.me/plus-one/food-rule-1-eat-food

Heroic Equipment
- Gymboss Plus Timer: https://www.amazon.com/dp/B07QK9WBW6/ref=twister_B08B1RMCZ7?_encoding=UTF8&psc=1
'''

'''

Sleep Medication Protocol

'''
IF READINESS < 70 {
    IF AVERAGE_WEEKLY_INTAKE < 50%
        takeMedicine('Gabapentin')
        IF ( DAYS_NOT_FULLY_RECOVERED > 1 )
            takeMedicine('Ativan')
    ELSE 
        contact(PSYCHIATRIST)
}