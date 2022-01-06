import { useEffect, useState } from "react";
import { Navigate, useParams } from "react-router-dom";

// Components
import check from "./check";
import SettingsForm from "./SettingsForm";

const Settings = () => {
  const [user, setUser] = useState("");
  const { id } = useParams();

  useEffect(() => {
    
  }, [id]);

  return (
    <div className="settings">
      
    </div>
  );
};

export default Settings;
