import {
  Link,
  useNavigate
} from "react-router-dom";


function Sidebar() {

    const navigate = useNavigate();

  return (

    <div className="w-64 bg-[#081028] text-white min-h-screen p-6">

      <h1 className="text-5xl font-bold mb-10">

        FinRisk AI

      </h1>


      <div className="space-y-5 text-xl">


        <li
  onClick={() => navigate("/")}
  className="
    cursor-pointer
    hover:text-cyan-400
    transition
  "
>

  Home

</li>

        <Link
          to="/dashboard"
          className="block hover:text-blue-400"
        >

          Dashboard

        </Link>


        <Link
          to="/live-monitoring"
          className="block hover:text-blue-400"
        >

          Live Monitoring

        </Link>


        <Link
          to="/fraud-analytics"
          className="block hover:text-blue-400"
        >

          Fraud Analytics

        </Link>


        <Link
          to="/ml-monitoring"
          className="block hover:text-blue-400"
        >

          ML Monitoring

        </Link>


        <Link
          to="/explainable-ai"
          className="block hover:text-blue-400"
        >

          Explainable AI

        </Link>


        <Link
          to="/project-overview"
          className="block hover:text-blue-400"
        >

          Project Overview

        </Link>

      </div>

    </div>
  );
}

export default Sidebar;