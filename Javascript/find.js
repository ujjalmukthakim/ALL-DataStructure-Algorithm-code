const users = [
    { id: 1, name: "John" },
    { id: 2, name: "David" }
];

const user = users.find(user => user.id === 2);

console.log(user);