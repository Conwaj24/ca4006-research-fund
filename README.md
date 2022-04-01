# CA4006 Assignment 2

Jordan Conway-McLuaghlin and Ciprian Hutanu
[demo video](./demo.webm)

## Instructions

run `make`

## Detailed instructions:

To use the program, open 2 terminal windows in the root of the git repository, or 1 terminal window, but run the first command in detached mode with "&".

In the first window:
`make`

Use the second window to send commands:
`./sendmessage <command goes here>`

Use commands below to perform various functions.

Command list:

`apply <research group name> <funding amount at the end, a number>`

`withdraw <amount> <group name> <researcher name>`

`add_researcher <group name> <researcher name>`

`add_description <group name> <description> (description can be space separated, no need for quotation marks)`

`get_description <group name>`

`add_title <group name> <title>`

`get_title <group name>`

## Design

The program is implemented as a number of independent scripts in a Unix-style approach to concurrency. It relies on the Linux shell and functions for communication, multithreading, and security (theoretically). Each unit is written as its own program and executed as its own process. Communication between threads is done in part with Named Pipes (FIFO's), and in part through ordinary files. Where ordinary files are used, Linux's mutual exclusion features make sure there aren't race conditions.
Care was taken to ensure the robustness of bank accounts as they are perhaps the most critical part in a real-world scenario. Bank accounts are implemented as a file showing the balance and the full transaction history, a withdrawl from the bank account is close to atomic (a single shell built-in) and the file is always appended to, never overwritten. All that is to say, the bank account it likely very robust to unexpected failures such as a power outage, and even if it is partially corrupted it could be reconstructed. The use of a filesytem like ZFS or BTRFS would make failure almost impossible. The bank account could also be checked routinely or before each transaction to ensure the number add up.

## Jordan's reflection

I learned a few interesting things about how concurrency works in Linux; there are surprisingly many ways to do concurrency built in to the OS, including a message queue which we didn't end up using because I wanted to keep it simple and using shell script. I also learned, not for the first time, that FIFO's are a pain to work with and they never see mto do what you want them to; they can certainly be used in a many-to-one or one-to-many context but they're really designed for synchronous communication between two process (which may have been evident from the name). the First-In-First-Out rule to which the FIFO owes its name is only true when a single process is writing to it, similarly with mutlitple readers it's random which one gets each line of output. It's also weirdly difficult to get a program to keep reading the pipe forever, even when there are no lines left, and it's weirdly difficult to read only a few lines from the pipe without consuming all the output. None of these things ended up mattering very much, luckily, and learning how FIFO's work is pretty handy because of how easy they are to use compared to other IPC methods. If I were to do it again, I would probably try to use message_queues even if it is more work, because it seems like less headache. I would also have wanted to have more elegant soultions to security and remote access; making this project the UNIX way allows us to hand-wave a lot of this stuff as of course "it's always theoretically possible" to use it in whatever manner you want, but it's a little annoying to need root privalages to add users and groups, or ssh to connect remote processes, a rest API certainly wouldn't have gone amiss.

## Ciprian's reflection

I learned about synchronous and asynchronous inter-process communication. This is something we’ve done in the past in a networking module at DCU, and but the first time was a broader overview. Previously, I’ve done this type of project exclusively in python, so with Jordan insisting we try do it in shell script (partially), I learned how versatile Linux built in functionality is. While we don’t have this running on separate systems, we could add a script to allow communication over the network, allowing cross-system communication. I contributed the python script which runs and listens for messages from the user, as well as the send_message script which simplifies the process for the user. I also designed the persistent data storage structure in “data/”. I’ve been struggling to keep up with all my work, so this is rushed. Had I had more time, or an opportunity at another time, I’d write the entire thing in Python, and include network functionality to allow other computers on the network to interact with the program. I try to avoid the excessive use of conditional statements in my code, as well as not having code duplication, so if I had the chance, I would spend time refactoring the code to my standards of code quality.
