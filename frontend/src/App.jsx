import { useEffect, useState } from "react";
import api from "./services/api";

import Login from "./components/Login";
import SearchBar from "./components/SearchBar";
import StudentForm from "./components/StudentForm";
import StudentTable from "./components/StudentTable";
import AIChat from "./components/AIChat";

function App() {
  const [loggedIn, setLoggedIn] = useState(
    localStorage.getItem("token") !== null
  );

  const [students, setStudents] = useState([]);

  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [major, setMajor] = useState("");

  const [editingId, setEditingId] = useState(null);
  const [search, setSearch] = useState("");

  useEffect(() => {
    if (loggedIn) {
      fetchStudents();
    }
  }, [loggedIn]);

  async function fetchStudents(studentName = "") {
    try {
      const response = await api.get("/students", {
        params: {
          name: studentName,
        },
      });

      setStudents(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function addStudent(e) {
    e.preventDefault();

    try {
      if (editingId === null) {
        await api.post("/students", {
          name,
          age: Number(age),
          major,
        });
      } else {
        await api.put(`/students/${editingId}`, {
          name,
          age: Number(age),
          major,
        });

        setEditingId(null);
      }

      setName("");
      setAge("");
      setMajor("");

      fetchStudents(search);

    } catch (error) {
      console.error(error);
    }
  }

  async function deleteStudent(id) {
    try {
      await api.delete(`/students/${id}`);

      fetchStudents(search);

    } catch (error) {
      console.error(error);
    }
  }

  function editStudent(student) {
    setEditingId(student.id);

    setName(student.name);
    setAge(student.age);
    setMajor(student.major);
  }

  function searchStudents(value = search) {
    fetchStudents(value);
  }

  function logout() {
    localStorage.removeItem("token");
    setLoggedIn(false);
  }

  if (!loggedIn) {
    return (
      <Login
        onLogin={() => setLoggedIn(true)}
      />
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <div className="max-w-6xl mx-auto">

        <div className="flex justify-between items-center mb-8">

          <h1 className="text-4xl font-bold text-blue-700">
            🎓 Student Management System
          </h1>

          <button
            onClick={logout}
            className="bg-red-600 hover:bg-red-700 text-white px-5 py-2 rounded"
          >
            Logout
          </button>

        </div>

        <SearchBar
          search={search}
          setSearch={setSearch}
          searchStudents={searchStudents}
        />

        <StudentForm
          name={name}
          age={age}
          major={major}
          setName={setName}
          setAge={setAge}
          setMajor={setMajor}
          addStudent={addStudent}
          editingId={editingId}
        />

        <StudentTable
          students={students}
          deleteStudent={deleteStudent}
          editStudent={editStudent}
        />

        {/* AI Assistant */}
        <AIChat />

      </div>

    </div>
  );
}

export default App;