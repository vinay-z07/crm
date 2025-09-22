import React, { useState } from "react";
import { Button, Input } from "@mui/material";

const Departments = () => {
  const [departments, setDepartments] = useState(["HR", "Sales", "Finance"]);
  const [newDept, setNewDept] = useState("");

  const addDepartment = () => {
    if (newDept.trim() !== "") {
      setDepartments([...departments, newDept]);
      setNewDept("");
    }
  };

  const deleteDepartment = (index) => {
    const updated = [...departments];
    updated.splice(index, 1);
    setDepartments(updated);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Departments</h2>
      <div style={{ display: "flex", gap: "10px" }}>
        <Input
          value={newDept}
          onChange={(e) => setNewDept(e.target.value)}
          placeholder="Enter department"
        />
        <Button variant="contained" onClick={addDepartment}>
          Add
        </Button>
      </div>

      <ul>
        {departments.map((dept, index) => (
          <li key={index} style={{ marginTop: "10px" }}>
            {dept}
            <Button
              size="small"
              color="error"
              onClick={() => deleteDepartment(index)}
              style={{ marginLeft: "10px" }}
            >
              Delete
            </Button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Departments;
