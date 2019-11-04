#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Loops infinitely with one second of step
 * Return: An int
**/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 * Return: 1 if couldn't fork, 0 if eveyrthing is ok
**/
int main(void)
{
	int i;
	pid_t zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid)
			printf("Zombie process created, PID: %d\n", zombie_pid);
		else
			return (0);
	}

	infinite_while();
	return (0);
}
