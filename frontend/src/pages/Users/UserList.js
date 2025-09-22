import React, { useState } from "react";
import {
  Button,
  Switch,
  Select,
  MenuItem,
  Input,
  Card,
  CardContent,
} from "@mui/material";

const roles = ["Admin", "Manager", "Staff", "Guest"];

const UserList = () => {
  const [users, setUsers] = useState([
    {
      name: "John Doe",
      dept: "Sales",
      designation: "Manager",
      email: "john@sales.com",
      phone: "9999999999",
      role: "Manager",
      active: true,
    },
  ]);

  const [newUser, setNewUser] = useState({
    name: "",
    dept: "",
    designation: "",
    email: "",
    phone: "",
    role: "Staff",
    active: true,
  });

  const addUser = () => {
    setUsers([...users, newUser]);
    setNewUser({
      name: "",
      dept: "",
      designation: "",
      email: "",
      phone: "",
      role: "Staff",
      active: true,
    });
  };

  const toggleActive = (index) => {
    const updated = [...users];
    updated[index].active = !updated[index].active;
    setUsers(updated);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>User Management</h2>
      <Card style={{ padding: "20px", marginBottom: "20px" }}>
        <h3>Add New User</h3>
        <Input
          placeholder="Name"
          value={newUser.name}
          onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
        />
        <Input
          placeholder="Department"
          value={newUser.dept}
          onChange={(e) => setNewUser({ ...newUser, dept: e.target.value })}
        />
        <Input
          placeholder="Designation"
          value={newUser.designation}
          onChange={(e) =>
            setNewUser({ ...newUser, designation: e.target.value })
          }
        />
        <Input
          placeholder="Email"
          value={newUser.email}
          onChange={(e) => setNewUser({ ...newUser, email: e.target.value })}
        />
        <Input
          placeholder="Phone"
          value={newUser.phone}
          onChange={(e) => setNewUser({ ...newUser, phone: e.target.value })}
        />

        <Select
          value={newUser.role}
          onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}
        >
          {roles.map((role, idx) => (
            <MenuItem key={idx} value={role}>
              {role}
            </MenuItem>
          ))}
        </Select>

        <Button variant="contained" style={{ marginLeft: "10px" }} onClick={addUser}>
          Add User
        </Button>
      </Card>

      <h3>Users</h3>
      {users.map((user, index) => (
        <Card key={index} style={{ marginBottom: "10px" }}>
          <CardContent>
            <p>
              <strong>{user.name}</strong> ({user.role})
            </p>
            <p>{user.email} | {user.phone}</p>
            <p>{user.dept} - {user.designation}</p>
            <Switch
              checked={user.active}
              onChange={() => toggleActive(index)}
            />
            {user.active ? "Active" : "Inactive"}
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default UserList;
