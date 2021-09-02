#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

void insertAfter(Node *prev_node, int data)
{
    if (prev_node->next == NULL)
    {
        return;
    }
    Node *new_node = new Node();
    new_node->data = data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}
void insertBefore(Node *before, int data)
{
    Node *temp = before->next;
    Node *new_node = new Node();
    before->next = new_node;
    new_node->data = data;
}
void append(Node **head, int data)
{
    Node *new_node = new Node();
    new_node->data = data;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = new_node;
}
void push(Node **head, int data)
{
    Node *new_node = new Node();
    new_node->data = data;
    if (*head == NULL)
        new_node->next = NULL;
    else
        new_node->next = *head;
    *head = new_node;
}
void printlist(Node *node)
{
    while (node != NULL)
    {
        cout << node->data << " ";
        node = node->next;
    }
}

int main()
{
    Node *head = NULL;
    append(&head, 6);
    push(&head, 7);
    push(&head, 1);
    append(&head, 4);
    insertAfter(head->next, 8);
    printlist(head);
    return 0;
}