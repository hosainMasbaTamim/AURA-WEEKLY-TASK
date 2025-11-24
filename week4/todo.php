

<?php
// db connection (using xampp)
$host = "localhost";
$user = "root";      // default in xampp
$pass = "";          // default empty
$db   = "todo_cli";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("connection failed: " . $conn->connect_error);
}

$cmd = $argv[1] ?? null;
$arg = $argv[2] ?? null;

switch ($cmd) {

    // add new task (C)
    case "add":
        if (!$arg) {
            echo "error! provide a task.\n";
            exit;
        }
        $stmt = $conn->prepare("INSERT INTO tasks (task) VALUES (?)");
        $stmt->bind_param("s", $arg);
        $stmt->execute();
        echo "added task: $arg\n";
        break;

    // list tasks (R)
    case "list":
        $result = $conn->query("SELECT * FROM tasks");
        if ($result->num_rows == 0) {
            echo "empty list.\n";
            exit;
        }
        while ($row = $result->fetch_assoc()) {
            $status = $row["done"] ? "[done]" : "[pending]";
            echo $row["id"] . ". $status " . $row["task"] . "\n";
        }
        break;

    // task done (E)
    case "done":
        if (!$arg) {
            echo "provide task no.\n";
            exit;
        }
        $stmt = $conn->prepare("UPDATE tasks SET done = 1 WHERE id = ?");
        $stmt->bind_param("i", $arg);
        $stmt->execute();
        echo "task done.\n";
        break;

    // delete task (D)
    case "del":
        if (!$arg) {
            echo "provide task no.\n";
            exit;
        }
        $stmt = $conn->prepare("DELETE FROM tasks WHERE id = ?");
        $stmt->bind_param("i", $arg);
        $stmt->execute();
        echo "task deleted.\n";
        break;

    // clear all tasks (E)
    case "clear":
        $conn->query("TRUNCATE TABLE tasks");
        echo "tasks cleared.\n";
        break;

    default:
        echo "CLI To-Do App Commands:\n";
        echo "  /opt/lampp/bin/php todo.php add \"task name\"\n";
        echo "  /opt/lampp/bin/php todo.php list\n";
        echo "  /opt/lampp/bin/php todo.php done <id>\n";
        echo "  /opt/lampp/bin/php todo.php del <id>\n";
        echo "  /opt/lampp/bin/php todo.php clear\n";
}
?>
