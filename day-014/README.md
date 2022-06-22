# The Higher-Lower game
## The easy way
- Use data provided from the course, as a list
- Function to randomly selected an entry, return data in 'name', 'follower_count', 'description' and 'country'
- Logic of the game, as a function
- A counter to count #(lives), a counter to record score
- A temp variable to hold the current data
- while loop while (#lives > 0)
- show game data and ask for input
- record input, update lives and scores

## Todos 
- [ ] (06-21-22) Fix the position of current entry in the `PrettyTable`
- [ ] (06-21-22) Update to web scrapping with Twitter count, the data provided by  Angela's course is *super outdated*.

## Organize
1. Generate a random account from the game data.
2. Format account data into printable format.
3. Ask user for a guess.
4. Check if user is correct.
    - Get follower count.
    - If Statement
5. Feedback.
6. Score Keeping.
7. Make game repeatable.
8. Make B become the next A.
9. Add art.
10. Clear screen between rounds.