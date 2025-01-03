Forked from https://github.com/Shogun89/fancy_job to make a Windows version.

# Shogun89's Daily Number Incrementer

A simple Python script that automatically increments a number in a text file,  commits the change to git and then pushes them. Perfect for maintaining a daily commit streak or tracking sequential values.

## Windows Setup

1. Clone this repository:

```bash
git clone https://github.com/shootweb/fancy_job
```

2. Set a new daily task in Task Scheduler:

> Open Task Scheduler.
> 
> Go to Action -> Create Basic Task...
> 
> Set a Name -> Next.
> 
> Set Trigger: "When I log on" or "When the Computer Starts" -> Next.
> 
> Set Action: Start a Program -> Next.
> 
> Click Browse... -> Select start.bat from the cloned directory.
>
> Click Finish.
> 
> Done!

This will run the script every time you log in as your user or when computer starts up (depending on the set trigger from step 2).

## Usage

The script will increment the number in `number.txt` and commit the change to git. You can modify the script to increment by any value or use a different file to store the number.

By running this you will be able get a fancy streak on your github profile and get a job.

![How to get a job](get_a_job.jpg)
