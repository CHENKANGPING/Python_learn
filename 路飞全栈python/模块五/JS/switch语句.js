switch (choice) {
      case "white":
        update("white", "black");
        break;
      case "black":
        update("black", "white");
        break;
      case "purple":
        update("purple", "white");
        break;
      case "yellow":
        update("yellow", "black");
        break;
      case "psychedelic":
        update("psychedelic", "white");
        break;
      default:
        update("white", "black");
    }