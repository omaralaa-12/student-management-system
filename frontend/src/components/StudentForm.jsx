function StudentForm({
  name,
  age,
  major,
  setName,
  setAge,
  setMajor,
  addStudent,
  editingId,
}) {
  return (
    <form
      onSubmit={addStudent}
      className="bg-white shadow rounded-lg p-6 mb-8"
    >
      <div className="grid grid-cols-3 gap-4">

        <input
          type="text"
          placeholder="Student Name"
          className="border p-3 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          type="number"
          placeholder="Age"
          className="border p-3 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />

        <input
          type="text"
          placeholder="Major"
          className="border p-3 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={major}
          onChange={(e) => setMajor(e.target.value)}
          required
        />

      </div>

      <button
        type="submit"
        className={`mt-4 px-6 py-3 rounded text-white font-semibold transition ${
          editingId === null
            ? "bg-blue-600 hover:bg-blue-700"
            : "bg-green-600 hover:bg-green-700"
        }`}
      >
        {editingId === null ? "➕ Add Student" : "💾 Update Student"}
      </button>

    </form>
  );
}

export default StudentForm;