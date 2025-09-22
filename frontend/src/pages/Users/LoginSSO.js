import React from "react";
import { Button } from "@mui/material";
import GoogleIcon from "@mui/icons-material/Google";
import MicrosoftIcon from "@mui/icons-material/Microsoft";

const LoginSSO = () => {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Login with SSO</h2>
      <Button
        variant="contained"
        color="error"
        startIcon={<GoogleIcon />}
        style={{ margin: "10px" }}
        onClick={() => alert("Google SSO Integration Placeholder")}
      >
        Google
      </Button>
      <Button
        variant="contained"
        color="primary"
        startIcon={<MicrosoftIcon />}
        style={{ margin: "10px" }}
        onClick={() => alert("Microsoft SSO Integration Placeholder")}
      >
        Microsoft 365
      </Button>
    </div>
  );
};

export default LoginSSO;
