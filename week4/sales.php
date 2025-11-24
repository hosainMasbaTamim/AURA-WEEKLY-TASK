<?php
// db connection
$host = "127.0.0.1";
$user = "root";
$pass = "";
$db   = "sales_cli";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
    die("connection failed: " . $conn->connect_error);
}

$cmd = $argv[1] ?? null;

switch ($cmd) {

    // add sale
    case "add":
        $product = $argv[2] ?? null;
        $quantity = $argv[3] ?? null;
        $price = $argv[4] ?? null;
        $date = $argv[5] ?? date('y-m-d');

        if (!$product || !$quantity || !$price) {
            echo "use proper format \n";
            exit;
        }

        $stmt = $conn->prepare("INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("sids", $product, $quantity, $price, $date);
        $stmt->execute();
        echo "sale added: $product ($quantity units at $price) on $date\n";
        break;

    // list sales
    case "list":
        $result = $conn->query("SELECT * FROM sales");
        if ($result->num_rows == 0) {
            echo "no sales found.\n";
            exit;
        }
        while ($row = $result->fetch_assoc()) {
            echo $row['id'] . ". " . $row['product'] . " | Qty: " . $row['quantity'] . " | Price: " . $row['price'] . " | Date: " . $row['sale_date'] . "\n";
        }
        break;

    // update sale
    case "update":
        $id = $argv[2] ?? null;
        $field = $argv[3] ?? null;
        $value = $argv[4] ?? null;

        if (!$id || !$field || !$value) {
            echo "use proper format\n";
            exit;
        }

        $stmt = $conn->prepare("UPDATE sales SET $field = ? WHERE id = ?");
        if ($field == 'quantity' || $field == 'price') {
            $stmt->bind_param("di", $value, $id);
        } else {
            $stmt->bind_param("si", $value, $id);
        }
        $stmt->execute();
        echo "sale $id updated.\n";
        break;

    // delete sale
    case "del":
        $id = $argv[2] ?? null;
        if (!$id) {
            echo "use proper format\n";
            exit;
        }
        $stmt = $conn->prepare("DELETE FROM sales WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        echo "sale $id deleted.\n";
        break;

    // clear sales
    case "clear":
        $conn->query("TRUNCATE TABLE sales");
        echo " sales cleared.\n";
        break;

    default:
        echo "CLI Sales Tracker Commands:\n";
        echo "  /opt/lampp/bin/php sales.php add \"product\" quantity price \"YYYY-MM-DD\"\n";
        echo "  /opt/lampp/bin/php sales.php list\n";
        echo "  /opt/lampp/bin/php sales.php update id field value\n";
        echo "  /opt/lampp/bin/php sales.php del id\n";
        echo "  /opt/lampp/bin/php sales.php clear\n";
}
?>
